#!/usr/bin/env bash
# Start all Onyx Interop runtime services
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PARENT_ROOT="$(cd "$PROJECT_ROOT/../.." && pwd)"
LOG_DIR="$PROJECT_ROOT/data/logs"
mkdir -p "$LOG_DIR"

if [ -f "$PROJECT_ROOT/.venv/bin/activate" ]; then
  source "$PROJECT_ROOT/.venv/bin/activate"
fi

FHIR_DATA="${FHIR_DATA:-$PARENT_ROOT/fhir_output/ndjson}"
PAA_DATA="${PAA_DATA:-$PROJECT_ROOT/../PAA+}"

echo "=== Starting Onyx Interop Services ==="

start_service() {
  local name="$1"
  local cmd="$2"
  local log="$LOG_DIR/${name}.log"
  if pgrep -f "$name" > /dev/null 2>&1; then
    echo "  SKIP  $name (already running)"
  else
    eval "$cmd" > "$log" 2>&1 &
    echo "  START $name (PID $!, log: $log)"
  fi
}

# Data pipeline if FHIR output missing
if [ ! -f "$FHIR_DATA/Patient.ndjson" ]; then
  echo "Running data pipeline first..."
  python3 "$PARENT_ROOT/interop_pipeline.py" --input "$PARENT_ROOT/source_data" --output "$PARENT_ROOT/fhir_output"
fi

start_service "slap_server" "python3 $PARENT_ROOT/slap_server.py --port 9000"
start_service "fhir_server" "python3 $PARENT_ROOT/fhir_server.py --port 8080 --data $FHIR_DATA"
start_service "onyx_insights" "python3 $PARENT_ROOT/onyx_insights_server.py --port 9001"
start_service "mdp_server" "python3 $PARENT_ROOT/mdp_server.py --port 9002"
start_service "provider_access" "python3 $PROJECT_ROOT/runtime/provider_access.py --port 9003 --data $PAA_DATA"
start_service "p2p_member_match" "python3 $PARENT_ROOT/p2p_member_match.py --port 9004"
start_service "epa_service" "python3 $PARENT_ROOT/epa_burden_reduction_service.py --port 9005"
start_service "developer_portal" "python3 $PARENT_ROOT/developer_portal.py --port 9010"

sleep 2
echo ""
echo "=== Service Health Check ==="
for port_name in "9000:SLAP" "8080:FITE" "9001:Insights" "9002:MDP" "9003:ProviderAccess" "9004:P2P" "9005:ePA" "9010:DevPortal"; do
  port="${port_name%%:*}"
  name="${port_name##*:}"
  if curl -sf "http://localhost:$port/" > /dev/null 2>&1 || \
     curl -sf "http://localhost:$port/health" > /dev/null 2>&1 || \
     curl -sf "http://localhost:$port/.well-known/smart-configuration" > /dev/null 2>&1 || \
     curl -sf "http://localhost:$port/fhir/metadata" > /dev/null 2>&1 || \
     curl -sf "http://localhost:$port/cds-services" > /dev/null 2>&1; then
    echo "  OK  $name (:$port)"
  else
    echo "  ??  $name (:$port) — may still be starting"
  fi
done

echo ""
echo "All services started. Logs in $LOG_DIR"
