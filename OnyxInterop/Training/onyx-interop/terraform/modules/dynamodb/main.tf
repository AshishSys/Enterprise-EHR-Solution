variable "environment" { type = string }
variable "project" { type = string }

resource "aws_dynamodb_table" "metadata_v1" {
  name         = "${var.project}-${var.environment}-metadata-v1"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "business_id"
  range_key    = "resource_type"

  attribute {
    name = "business_id"
    type = "S"
  }
  attribute {
    name = "resource_type"
    type = "S"
  }

  tags = { Purpose = "Business ID to FHIR ID mapping" }
}

resource "aws_dynamodb_table" "onyx_job_state" {
  name         = "${var.project}-${var.environment}-job-state"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "workflow_family"
  range_key    = "run_id"

  attribute {
    name = "workflow_family"
    type = "S"
  }
  attribute {
    name = "run_id"
    type = "S"
  }

  tags = { Purpose = "Incremental load watermarks" }
}

output "metadata_table_name" { value = aws_dynamodb_table.metadata_v1.name }
output "job_state_table_name" { value = aws_dynamodb_table.onyx_job_state.name }
