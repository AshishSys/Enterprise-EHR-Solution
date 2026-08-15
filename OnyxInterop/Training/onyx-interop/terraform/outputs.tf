output "bronze_bucket" {
  value = module.s3.bronze_bucket_name
}

output "silver_bucket" {
  value = module.s3.silver_bucket_name
}

output "gold_bucket" {
  value = module.s3.gold_bucket_name
}

output "fhir_exports_bucket" {
  value = module.s3.fhir_exports_bucket_name
}

output "deid_bucket" {
  value = module.s3.deid_bucket_name
}

output "observability_bucket" {
  value = module.s3.observability_bucket_name
}

output "metadata_table" {
  value = module.dynamodb.metadata_table_name
}

output "job_state_table" {
  value = module.dynamodb.job_state_table_name
}

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "documentdb_endpoint" {
  value     = module.documentdb.cluster_endpoint
  sensitive = true
}

output "api_gateway_url" {
  value = module.apigateway.api_url
}
