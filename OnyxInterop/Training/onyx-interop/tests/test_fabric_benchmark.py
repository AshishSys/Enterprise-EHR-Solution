"""Fabric vs Databricks bake-off tests."""

from pipeline.fabric_benchmark import FabricBenchmark


def test_compare_picks_winners():
    bench = FabricBenchmark()
    db = bench.estimate_databricks(400, dbus=4)
    fab = bench.estimate_fabric(800, capacity_cu=64)
    result = bench.compare("clinical", rows=500_000, databricks=db, fabric=fab)
    assert result["winner_speed"] == "databricks"
    assert result["input_contract"] == "deid_sam"
    assert result["databricks"]["cost_per_million_rows"] > 0
