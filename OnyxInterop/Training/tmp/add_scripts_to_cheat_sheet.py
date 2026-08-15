#!/usr/bin/env python3
"""Inject **Script:** sections into Healthcare Interop Interview Cheat Sheet."""

from __future__ import annotations

import re
from pathlib import Path

CHEAT_SHEET = Path("/Users/ashishsingh/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md")
BASE = "/Users/ashishsingh/OnyxInterop/Training/onyx-interop"

SECTION_ROLES: dict[str, str] = {
    "A": "Associate Solution Architect | Forward Deployed Engineer",
    "B": "FHIR Engineer | Associate Solution Architect",
    "C": "Associate Solution Architect | Forward Deployed Engineer",
    "D": "Data Engineer | Intermediate Associate Programmer",
    "E": "FHIR Engineer | Intermediate Associate Programmer",
    "F": "Forward Deployed Engineer | Intermediate Associate Programmer",
    "G": "FHIR Engineer | Data Engineer",
    "H": "FHIR Engineer | Associate Solution Architect",
    "I": "Forward Deployed Engineer | Intermediate Associate Programmer",
    "J": "Data Engineer | Associate Solution Architect",
    "K": "Associate Solution Architect | FHIR Engineer",
    "L": "Forward Deployed Engineer | Associate Solution Architect",
    "M": "Forward Deployed Engineer | Associate Solution Architect",
    "N": "Data Engineer | Intermediate Associate Programmer",
    "O": "AI Engineer | Intermediate Associate Programmer",
    "P": "Data Engineer | Kafka Engineer",
    "Q": "Data Engineer | Intermediate Associate Programmer",
    "R": "AI Engineer | Data Engineer",
    "S": "Data Engineer | Intermediate Associate Programmer",
    "T": "Associate Solution Architect | Data Engineer",
    "U": "Data Engineer | AI Engineer | Intermediate Associate Programmer",
    "V": "Data Engineer | Associate Solution Architect",
    "W": "Data Engineer | Associate Solution Architect",
    "X": "Data Engineer | Intermediate Associate Programmer",
    "Y": "AI Engineer | Forward Deployed Engineer",
}


def section_for_q(q_num: int) -> str:
    if q_num <= 10:
        return "A"
    if q_num <= 28:
        return "B"
    if q_num <= 45:
        return "C"
    if q_num <= 73:
        return "D"
    if q_num <= 94:
        return "E"
    if q_num <= 112:
        return "F"
    if q_num <= 124:
        return "G"
    if q_num <= 141:
        return "H"
    if q_num <= 154:
        return "I"
    if q_num <= 162:
        return "J"
    if q_num <= 172:
        return "K"
    if q_num <= 185:
        return "L"
    if q_num <= 195:
        return "M"
    if q_num <= 205:
        return "N"
    if q_num <= 250:
        return "O"
    if q_num <= 295:
        return "P"
    if q_num <= 330:
        return "Q"
    if q_num <= 360:
        return "R"
    if q_num <= 390:
        return "S"
    if q_num <= 415:
        return "T"
    if q_num <= 445:
        return "U"
    if q_num <= 455:
        return "V"
    if q_num <= 465:
        return "W"
    if q_num <= 473:
        return "X"
    return "Y"


def pick_script(q_num: int, title: str) -> str:
    t = title.lower()
    sec = section_for_q(q_num)
    roles = SECTION_ROLES[sec]

    # --- keyword-first overrides ---
    if any(k in t for k in ("kafka", "sqs", "webhook", "event stream", "firehose", "pub/sub", "nasco")):
        return kafka_script(q_num, t, roles)
    if any(k in t for k in ("de-id", "deident", "safe harbor", "expert determination", "tokenize", "phi")):
        return auth_script(q_num, t, roles)
    if any(k in t for k in ("mdm", "golden", "survivorship", "crosswalk", "ahima", "iso 8000")):
        return databricks_script(q_num, t, roles)
    if any(k in t for k in ("observability", "rca", "anomaly", "otel", "handoff")):
        return ai_script(q_num, t, roles)
    if any(k in t for k in ("rag", "vector", "mlflow", "agent", "mcp", "gateway", "embedding", "model")):
        return ai_script(q_num, t, roles)
    if any(k in t for k in ("fhir", "us core", "carin", "davinci", "da vinci", "bundle", "firely", "healthlake", "profile", "ig")):
        return fhir_script(q_num, t, roles)
    if any(k in t for k in ("slap", "oauth", "smart", "token", "pkce", "auth", "security", "rls", "mask")):
        return auth_script(q_num, t, roles)
    if any(k in t for k in ("terraform", "helm", "seiji", "deploy", "eks", "canary", "docker")):
        return deploy_script(q_num, t, roles)
    if any(k in t for k in ("fabric", "lakehouse", "power bi", "dataflow gen", "semantic")):
        return fabric_script(q_num, t, roles)
    if any(k in t for k in ("bigquery", "dataplex", "dataflow", "gcp", "cloud storage")):
        return gcp_script(q_num, t, roles)
    if any(k in t for k in ("merge", "sql", "index", "temporal", "partition", "t-sql", "vector_distance")):
        return sql_script(q_num, t, roles)
    if any(k in t for k in ("autoloader", "databricks", "delta", "liquid", "optimize", "vacuum", "unity catalog", "dab")):
        return databricks_script(q_num, t, roles)

    # --- section defaults ---
    defaults = {
        "A": platform_script,
        "B": fhir_script,
        "C": arch_script,
        "D": databricks_script,
        "E": fhir_script,
        "F": auth_script,
        "G": fhir_script,
        "H": fhir_script,
        "I": deploy_script,
        "J": metrics_script,
        "K": vbc_script,
        "L": leadership_script,
        "M": scenario_script,
        "N": fabric_script,
        "O": ai_script,
        "P": kafka_script,
        "Q": databricks_script,
        "R": ai_script,
        "S": fabric_script,
        "T": gcp_script,
        "U": sql_script,
        "V": auth_script,
        "W": databricks_script,
        "X": fabric_script,
        "Y": ai_script,
    }
    return defaults[sec](q_num, t, roles)


def wrap(roles: str, lang: str, body: str) -> str:
    body = body.strip("\n")
    return f"\n**Script:** *(builds proficiency: {roles})*\n\n```{lang}\n{body}\n```\n"


def platform_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: End-to-end platform proficiency drill
set -euo pipefail
cd {BASE}
./scripts/phase0_access_checklist.sh
./scripts/run_local_baseline.sh
python interop_pipeline.py --input ./source_data --output ./fhir_output
python scripts/validate_fhir_output.py ./fhir_output
python -m pytest tests/ -v --tb=short -k "test_" | tee /tmp/q{q}_pytest.log
echo "Q{q} baseline: $(find ./fhir_output -name '*.json' | wc -l) FHIR files validated"
""")


def arch_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: Architecture trace — map components to repos
set -euo pipefail
cd {BASE}
echo "=== Abacus data plane ==="
ls -1 pipeline/*.py configs/workflows/*/extract_config.yaml 2>/dev/null
echo "=== Onyx API plane ==="
ls -1 runtime/*.py apis/consumer/*.py helm/firely-server/values.yaml 2>/dev/null
echo "=== MDP registry ==="
python3 -c "import json; r=json.load(open('configs/mdp/services.json')); print(json.dumps(r, indent=2)[:800])"
curl -sf http://localhost:9002/services 2>/dev/null || echo "Start stack: ./scripts/start_all_services.sh"
""")


def fhir_script(q: int, t: str, roles: str) -> str:
    patient = "Patient/example"
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: FHIR validation + API read proficiency
set -euo pipefail
cd {BASE}
python scripts/validate_fhir_output.py ./fhir_output --strict 2>&1 | tee /tmp/q{q}_fhir_validation.log

# Capability + resource read (requires local stack)
curl -sf http://localhost:8080/metadata | python3 -m json.tool | head -40
curl -sf "http://localhost:8080/{patient}" -H "Authorization: Bearer ${{TOKEN:-demo}}" | python3 -m json.tool | head -30

# Count resources by type in generated output
python3 << 'PY'
import json, pathlib, collections
c = collections.Counter()
for p in pathlib.Path("./fhir_output").rglob("*.json"):
    try:
        d = json.loads(p.read_text())
        if d.get("resourceType"): c[d["resourceType"]] += 1
        elif d.get("entry"):
            for e in d["entry"]:
                rt = e.get("resource", {{}}).get("resourceType")
                if rt: c[rt] += 1
    except Exception: pass
for rt, n in sorted(c.items()): print(f"{{rt}}: {{n}}")
print(f"TOTAL types: {{len(c)}}")
PY
""")


def databricks_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "python", f"""# Q{q}: Databricks/Delta proficiency — run in notebook or local Spark
from pyspark.sql import functions as F

# Bronze → Silver pattern (Rail C FHIR NDJSON)
bronze = spark.read.format("cloudFiles") \\
    .option("cloudFiles.format", "json") \\
    .option("cloudFiles.schemaLocation", "s3://interop/bronze/_schemas/fhir/") \\
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns") \\
    .load("s3://interop/landing/pulseehr/fhir/")

silver = bronze.filter(F.col("resourceType").isNotNull()) \\
    .withColumn("profile_match", F.expr("validate_uscore(resource)")) \\
    .filter(F.col("profile_match") == True)

silver.write.format("delta").mode("append").saveAsTable("prod_interop.silver.fhir_resources")

# Check + optimize
display(spark.sql("SELECT resourceType, COUNT(*) c FROM prod_interop.silver.fhir_resources GROUP BY 1 ORDER BY c DESC"))
spark.sql("OPTIMIZE prod_interop.sam.clinical.conditions")
spark.sql("DESCRIBE HISTORY prod_interop.sam.clinical.conditions").show(5, truncate=False)
print("Q{q} Delta pipeline checkpoint OK")
""")


def auth_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: SMART on FHIR / SLAP token flow
set -euo pipefail
SLAP="${{SLAP_URL:-http://localhost:9000}}"
CLIENT_ID="${{CLIENT_ID:-demo-app}}"
REDIRECT="http://localhost:3000/callback"
CODE_VERIFIER="$(openssl rand -base64 32 | tr -d '=+/ ' | cut -c1-43)"
CODE_CHALLENGE="$(printf '%s' "$CODE_VERIFIER" | openssl dgst -sha256 -binary | openssl base64 -A | tr '+/' '-_' | tr -d '=')"

echo "=== SMART authorize (PKCE S256) ==="
AUTH_URL="$SLAP/oauth/authorize?response_type=code&client_id=$CLIENT_ID&redirect_uri=$REDIRECT&scope=patient/Patient.read&code_challenge=$CODE_CHALLENGE&code_challenge_method=S256"
echo "$AUTH_URL"

# After user login, exchange code:
# curl -X POST "$SLAP/oauth/token" -d "grant_type=authorization_code&code=CODE&redirect_uri=$REDIRECT&client_id=$CLIENT_ID&code_verifier=$CODE_VERIFIER"

curl -sf "$SLAP/.well-known/smart-configuration" | python3 -m json.tool || echo "Start SLAP: cd {BASE} && python slap_server.py"
""")


def deploy_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: Forward-deployed deploy + verify
set -euo pipefail
cd {BASE}/terraform
terraform init -backend=false 2>/dev/null || true
terraform validate
terraform plan -var-file=dev.tfvars -out=/tmp/q{q}.tfplan 2>/dev/null || terraform plan

cd {BASE}
helm lint helm/firely-server/
helm template firely helm/firely-server/ -f helm/firely-server/values.yaml | head -60

# K8s health (when cluster available)
kubectl get pods -n firely 2>/dev/null || echo "Configure kubeconfig for EKS"
kubectl rollout status deployment/firely-server -n firely --timeout=120s 2>/dev/null || true
echo "Q{q} deploy artifacts validated"
""")


def kafka_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "python", f"""# Q{q}: Kafka/event-stream proficiency (Rail B pattern)
# Producer — partner webhook → Kafka (MSK) after Lambda validation
from confluent_kafka import Producer, Consumer, KafkaException
import json, os

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = "interop.claim.adjudicated.v1"

def delivery_report(err, msg):
    if err: raise KafkaException(err)

p = Producer({{"bootstrap.servers": BOOTSTRAP, "client.id": "nasco-webhook-producer"}})
event = {{
    "event_id": "evt-q{q}-001",
    "payer_id": "UHC",
    "member_id": "M12345",
    "claim_id": "C98765",
    "adjudication_date": "2025-07-19",
    "status": "final"
}}
p.produce(TOPIC, key=event["claim_id"], value=json.dumps(event), callback=delivery_report)
p.flush()

# Consumer — Autoloader/Firehose downstream reads from S3; this verifies Kafka path
c = Consumer({{
    "bootstrap.servers": BOOTSTRAP,
    "group.id": "interop-bronze-loader-q{q}",
    "auto.offset.reset": "earliest"
}})
c.subscribe([TOPIC])
msg = c.poll(5.0)
if msg and not msg.error():
    print("Consumed:", msg.key(), msg.value().decode()[:200])
c.close()
""")


def ai_script(q: int, t: str, roles: str) -> str:
    body = f"""# Q{q}: AI Engineer — RAG + agent event detection
import mlflow
from databricks.vector_search.client import VectorSearchClient

# Log a governed inference run
with mlflow.start_run(run_name="q{q}_pas_scoring"):
    mlflow.log_param("ig_version", "davinci-pas-2.0.1")
    mlflow.log_param("model_stage", "Production")
    mlflow.log_metric("auc", 0.87)

# RAG retrieval for formulary policy Q&A
vsc = VectorSearchClient()
idx = vsc.get_index(endpoint_name="interop_vs", index_name="prod_interop.ai.formulary_policy_idx")
results = idx.similarity_search(
    query_text="Is prior auth required for Humira?",
    columns=["ndc", "policy_text", "pa_required"],
    num_results=5
)
for row in results.get("result", dict()).get("data_array", []):
    print(row)

# ai_events queue insert (Payer Ops Agent input)
spark.sql('''
INSERT INTO prod_interop.sam.ai_events.event_queue
  (event_id, actor_type, severity, event_type, summary, source_table, created_at)
VALUES
  ('evt-q{q}', 'PAYER_OPS', 'WARN', 'INGESTION_LAG',
   'Bronze lag 4h for pulse-ehr', 'prod_interop.bronze.fhir_ndjson', current_timestamp())
''')
print("Q{q} AI pipeline events + RAG retrieval OK")
"""
    return wrap(roles, "python", body)


def fabric_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "python", f"""# Q{q}: Microsoft Fabric Lakehouse proficiency
# Run in Fabric notebook — CMS metrics mirror from Databricks export
from pyspark.sql import functions as F

# OneLake shortcut to ADLS export (no duplicate copy)
cms = spark.read.format("parquet").load("abfss://exports@datalake/metrics/cms/")
cms.groupBy("payer_id", "api_family").agg(
    F.avg("uptime_pct").alias("avg_uptime"),
    F.sum("api_calls").alias("total_calls")
).orderBy("payer_id").show()

# Type 2 SCD hash compare for eligibility
from pyspark.sql.functions import sha2, concat_ws, lit
staging = spark.table("eligibility_staging")
staging = staging.withColumn(
    "row_hash",
    sha2(concat_ws("|", "member_id", "plan_id", "effective_date", "benefit_tier"), 256)
)
staging.write.mode("overwrite").saveAsTable("eligibility_staging_hashed")
print("Q{q} Fabric CMS metrics + SCD hash staging complete")
""")


def gcp_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: GCP hybrid reference — BigQuery CMS rollup
set -euo pipefail
# Scheduled query pattern (run via bq CLI)
bq query --use_legacy_sql=false << 'SQL'
CREATE OR REPLACE TABLE cms.monthly_patient_access_sla AS
SELECT
  payer_id,
  DATE_TRUNC(metric_date, MONTH) AS metric_month,
  AVG(uptime_pct) AS avg_uptime_pct,
  COUNTIF(uptime_pct < 99.0) AS breach_hours
FROM cms.hourly_api_metrics
WHERE metric_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 13 MONTH)
GROUP BY 1, 2;
SQL

bq show --format=prettyjson cms.monthly_patient_access_sla | head -30
echo "Q{q} GCP CMS rollup validated"
""")


def sql_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "sql", f"""-- Q{q}: Azure SQL / T-SQL proficiency
-- RLS + masked member access + incremental MERGE

EXEC sp_set_session_context @key = N'payer_id', @value = N'UHC';

-- Row-level security enforced
SELECT COUNT(*) AS visible_claims FROM dbo.claims_summary;

-- Idempotent claim line upsert from Rail A staging
BEGIN TRY
  BEGIN TRAN;
  MERGE dbo.claim_line AS t
  USING staging.claim_line AS s
    ON t.claim_id = s.claim_id AND t.line_number = s.line_number
  WHEN MATCHED AND CHECKSUM(t.billed_amount, t.paid_amount) <> CHECKSUM(s.billed_amount, s.paid_amount)
    THEN UPDATE SET t.billed_amount = s.billed_amount, t.paid_amount = s.paid_amount, t.modified_utc = SYSUTCDATETIME()
  WHEN NOT MATCHED THEN
    INSERT (claim_id, line_number, member_id, billed_amount, paid_amount, modified_utc)
    VALUES (s.claim_id, s.line_number, s.member_id, s.billed_amount, s.paid_amount, SYSUTCDATETIME());
  COMMIT;
END TRY
BEGIN CATCH
  IF @@TRANCOUNT > 0 ROLLBACK;
  THROW;
END CATCH;

-- Vector similarity for formulary alternatives
SELECT TOP 5 ndc, description,
  VECTOR_DISTANCE('cosine', embedding, @query_embedding) AS distance
FROM dbo.formulary_drug
ORDER BY distance;
""")


def metrics_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "python", f"""# Q{q}: CMS metrics reporting proficiency
import json, urllib.request
# Local Insights endpoint
try:
    resp = urllib.request.urlopen("http://localhost:9001/metrics/cms/patient-access")
    data = json.loads(resp.read())
    print(json.dumps(data, indent=2)[:1000])
except Exception as e:
    print("Start Insights:", e)

# Reporter script
import subprocess
subprocess.run(["python", "{BASE}/monitoring/cms_metrics_reporter.py", "--dry-run"], check=False)
""")


def vbc_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "sql", f"""-- Q{q}: VBC bridge — reuse SAM for quality gaps
SELECT m.member_id,
       COUNT(DISTINCT CASE WHEN o.code LOINC IN ('4548-4','17856-6') THEN o.observation_id END) AS a1c_count,
       MAX(c.service_date) AS last_pcp_visit
FROM clinical_sam.members m
LEFT JOIN clinical_sam.observations o ON m.member_id = o.member_id
LEFT JOIN claims_sam.encounters c ON m.member_id = c.member_id AND c.type = 'PCP'
GROUP BY m.member_id
HAVING a1c_count = 0 OR last_pcp_visit < DATEADD(month, -12, GETDATE());
""")


def leadership_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: Solution architect / leader — phase exit criteria audit
set -euo pipefail
cd {BASE}
echo "=== Phase exit checklist Q{q} ==="
python -m pytest tests/ -q --co | wc -l | xargs -I{{}} echo "Test cases defined: {{}}"
./scripts/phase0_access_checklist.sh 2>/dev/null | tail -5 || true
test -f configs/mdp/ig_registry.json && echo "IG registry: OK" || echo "IG registry: MISSING"
grep -c "status: pending\\|status: in_progress\\|status: completed" {BASE}/../.cursor/plans/*.plan.md 2>/dev/null || true
""")


def scenario_script(q: int, t: str, roles: str) -> str:
    return wrap(roles, "bash", f"""#!/usr/bin/env bash
# Q{q}: Scenario drill — reproduce, diagnose, fix
set -euo pipefail
cd {BASE}
LOG="/tmp/q{q}_scenario.log"
{{
  echo "=== 1. Reproduce ==="
  python interop_pipeline.py --input ./source_data --output ./fhir_output 2>&1
  echo "=== 2. Validate ==="
  python scripts/validate_fhir_output.py ./fhir_output 2>&1
  echo "=== 3. Runtime smoke ==="
  curl -sf http://localhost:8080/metadata >/dev/null && echo "FITE OK" || echo "FITE DOWN"
  curl -sf http://localhost:9000/.well-known/smart-configuration >/dev/null && echo "SLAP OK" || echo "SLAP DOWN"
}} | tee "$LOG"
echo "Scenario log: $LOG"
""")


def inject_scripts(content: str) -> tuple[str, int]:
    if "**Script:**" in content and content.count("**Script:**") >= 400:
        return content, 0

    pattern = re.compile(r"(### Q(\d+)\.[^\n]+\n(?:.*?\n)*?)(?=\n### Q|\n## Section |\Z)", re.DOTALL)
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        block = match.group(1)
        q_num = int(match.group(2))
        if "**Script:**" in block:
            return block
        title_match = re.search(r"### Q\d+\.\s*(.+)", block)
        title = title_match.group(1).strip() if title_match else ""
        script = pick_script(q_num, title)
        # Insert after last How to Fix bullet block
        lines = block.rstrip().split("\n")
        insert_at = len(lines)
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].startswith("**How to Fix:**"):
                insert_at = i + 1
                while insert_at < len(lines) and (lines[insert_at].startswith("- ") or lines[insert_at].strip() == ""):
                    insert_at += 1
                break
        new_lines = lines[:insert_at] + [script.rstrip()] + lines[insert_at:]
        count += 1
        return "\n".join(new_lines) + "\n"

    new_content = pattern.sub(replacer, content)
    return new_content, count


def main() -> None:
    text = CHEAT_SHEET.read_text(encoding="utf-8")
    new_text, n = inject_scripts(text)
    CHEAT_SHEET.write_text(new_text, encoding="utf-8")
    script_count = new_text.count("**Script:**")
    print(f"Injected scripts into {n} questions; total Script sections: {script_count}")


if __name__ == "__main__":
    main()
