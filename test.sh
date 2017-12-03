# Query results
#curl 127.0.0.1:5000/secret | jq '.[]."secret_code"'
curl 127.0.0.1:5000 | jq -r .[]."secret_code"
