output "terraform_queue" {
  value = aws_sqs_queue.terraform_queue.arn
}

output "terraform_queue_deadletter" {
  value = aws_sqs_queue.terraform_queue_deadletter.arn
}