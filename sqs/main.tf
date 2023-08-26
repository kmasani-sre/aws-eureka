resource "aws_sqs_queue" "terraform_queue" {
  name                      = "km-sqs-example-queue"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10

  tags = {
    Environment = var.environment
  }
}

resource "aws_sqs_queue_redrive_policy" "terraform_queue_policy" {
  queue_url = aws_sqs_queue.terraform_queue.id
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.terraform_queue_deadletter.arn
    maxReceiveCount     = 4
  })

}

resource "aws_sqs_queue" "terraform_queue_deadletter" {
  name                  = "km-sqs-example-deadletter-queue"
  redrive_allow_policy  = jsonencode({
    redrivePermission   = "byQueue",
    sourceQueueArns     = [aws_sqs_queue.terraform_queue.arn]
  })

  tags = {
    Environment = var.environment
  }
}