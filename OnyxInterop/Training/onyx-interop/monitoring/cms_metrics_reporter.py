#!/usr/bin/env python3
"""CMS Patient Access metrics reporter for CloudWatch compliance."""

import json
import time
from datetime import datetime, timezone


class CMSMetricsReporter:
    """Reports CMS-0057 mandated Patient Access API metrics."""

    METRICS = [
        "api_requests_total",
        "api_requests_success",
        "api_requests_error",
        "auth_success_total",
        "auth_failure_total",
        "avg_response_time_ms",
        "p95_response_time_ms",
        "unique_members_accessed",
        "bulk_export_jobs_total",
    ]

    def __init__(self, namespace: str = "OnyxInterop/CMS"):
        self.namespace = namespace
        self.metrics = {m: 0 for m in self.METRICS}
        self.response_times = []

    def record_request(self, endpoint: str, status_code: int, latency_ms: float, member_id: str = None):
        self.metrics["api_requests_total"] += 1
        if 200 <= status_code < 400:
            self.metrics["api_requests_success"] += 1
        else:
            self.metrics["api_requests_error"] += 1
        self.response_times.append(latency_ms)
        if member_id:
            self.metrics.setdefault("_members", set()).add(member_id)

    def record_auth(self, success: bool):
        key = "auth_success_total" if success else "auth_failure_total"
        self.metrics[key] += 1

    def record_bulk_export(self):
        self.metrics["bulk_export_jobs_total"] += 1

    def compute_aggregates(self):
        if self.response_times:
            self.metrics["avg_response_time_ms"] = sum(self.response_times) / len(self.response_times)
            sorted_times = sorted(self.response_times)
            idx = int(len(sorted_times) * 0.95)
            self.metrics["p95_response_time_ms"] = sorted_times[min(idx, len(sorted_times) - 1)]
        members = self.metrics.pop("_members", set())
        self.metrics["unique_members_accessed"] = len(members)

    def to_cloudwatch_payload(self) -> list[dict]:
        self.compute_aggregates()
        timestamp = datetime.now(timezone.utc)
        return [
            {
                "MetricName": name,
                "Value": value,
                "Unit": "Count" if "total" in name or "accessed" in name else "Milliseconds",
                "Timestamp": timestamp.isoformat(),
                "Dimensions": [{"Name": "Environment", "Value": "production"}],
            }
            for name, value in self.metrics.items()
            if isinstance(value, (int, float))
        ]

    def publish(self, cloudwatch_client=None):
        payload = self.to_cloudwatch_payload()
        if cloudwatch_client:
            for metric in payload:
                cloudwatch_client.put_metric_data(Namespace=self.namespace, MetricData=[metric])
        return payload


if __name__ == "__main__":
    reporter = CMSMetricsReporter()
    reporter.record_request("/fhir/Patient", 200, 45.2, "patient-001")
    reporter.record_request("/fhir/Patient/001/$everything", 200, 120.5, "patient-001")
    reporter.record_auth(True)
    reporter.record_auth(False)
    print(json.dumps(reporter.to_cloudwatch_payload(), indent=2))
