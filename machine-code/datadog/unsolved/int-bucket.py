'''
"int in bucket"
We need to group a list of integers according to a specified bucket width and count the number of numbers in each bucket.
Rules: Bucket boundaries:
1st bucket: [0, bucket_width - 1]
2nd bucket: [bucket_width, 2 * bucket_width - 1]
Nth bucket: [N * bucket_width, (N+1) * bucket_width - 1]
Last bucket: Stores all numbers greater than or equal to the upper bound of the last bucket. Bucket number calculation: Calculate num // bucket_width to get the bucket number. If the number >= num_buckets - 1, then put it into the last bucket.
'''