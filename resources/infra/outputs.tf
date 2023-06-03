# Output the API Gateway endpoint URL
output "api_gateway_endpoint" {
  value = aws_api_gateway_deployment.api_gateway_deployment.invoke_url
}
