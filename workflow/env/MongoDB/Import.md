mongoimport --type csv --file filename --headerline

--upsertFields <field1[,field2]>
To ensure adequate performance, indexes should exist for this field or fields.

mongoimport --db rates --collection kaggle --type csv --columnsHaveTypes --fields "name.string(),birthdate.date(2006-01-02),contacted.boolean(),followerCount.int32(),user thumbnail.binary(base64)" --file /data/file.csv
