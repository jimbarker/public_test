import boto3
# Pre-amble
print("## Purpose")
print("The purpose of this page is to maintain a mapping of which DataWorks S3 buckets are used for what purpose.\n")
# List of environments
environments = ["Development",
                "QA",
                "Integration",
                "Preprod",
                "Production",
                "Management-Dev",
                "Management"]
# Get a list of buckets for each environment
for environment in environments:
    print("## {0}\n".format(environment))
    print("| Bucket ID                        | Name |")
    print("| -------------------------------- | ---- |")
    aws_profile = "dataworks-{0}".format((environment).lower())
    aws_session = boto3.Session(profile_name=aws_profile)
    s3_client = aws_session.client('s3')
    response = s3_client.list_buckets()
    # Find the name tag for each bucket in each environment
    for bucket in response['Buckets']:
        bucket_id = bucket['Name']
        try:
            bucket_tagging = s3_client.get_bucket_tagging(Bucket=bucket_id)
        except:
            bucket_name_tag = "Bucket has no tags set!"
        else:
            tag_set = bucket_tagging['TagSet']
            bucket_name_tag = "Bucket has no name tag!"
            for tag in tag_set:
                if tag["Key"].lower() == "name":
                    bucket_name_tag = tag["Value"]
        # Print a list of bucket names
        print("| {0} | {1} |".format(bucket_id, bucket_name_tag))
    print("\n\n")
    