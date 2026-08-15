variable "environment" { type = string }
variable "project" { type = string }

resource "aws_s3_bucket" "bronze" {
  bucket = "${var.project}-${var.environment}-raw-bronze"
}

resource "aws_s3_bucket" "silver" {
  bucket = "${var.project}-${var.environment}-processed-silver"
}

resource "aws_s3_bucket" "gold" {
  bucket = "${var.project}-${var.environment}-gold-analytics"
}

resource "aws_s3_bucket" "fhir_exports" {
  bucket = "${var.project}-${var.environment}-fhir-exports"
}

resource "aws_s3_bucket" "scripts" {
  bucket = "${var.project}-${var.environment}-scripts"
}

resource "aws_s3_bucket" "deid" {
  bucket = "${var.project}-${var.environment}-deid-safe-harbor"
}

resource "aws_s3_bucket" "observability" {
  bucket = "${var.project}-${var.environment}-observability-deid"
}

resource "aws_s3_bucket_versioning" "versioning" {
  for_each = aws_s3_bucket
  bucket   = each.value.id
  versioning_configuration { status = "Enabled" }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  for_each = aws_s3_bucket
  bucket   = each.value.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

output "bronze_bucket_name" { value = aws_s3_bucket.bronze.id }
output "silver_bucket_name" { value = aws_s3_bucket.silver.id }
output "gold_bucket_name" { value = aws_s3_bucket.gold.id }
output "fhir_exports_bucket_name" { value = aws_s3_bucket.fhir_exports.id }
output "deid_bucket_name" { value = aws_s3_bucket.deid.id }
output "observability_bucket_name" { value = aws_s3_bucket.observability.id }
