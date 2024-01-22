# despina
This microservice is used to convert large bodies of text from payload and convert it into a model readable format. Which would then be saved into a minio s3 bucket or ftp. This file would be used further downstream by the fine-tuning microservice to be able to train the model and manage the life-cycle of the module. 

[Deprecated] This is the model fine tuning microservice. It is responsible for managing the lifetime of the fine-tuned models. It defines endpoints to take in file input, text input or conversation input and converts it into training data for any preselected model. The model is fine-tuned using the training data and then the id of the model is stored along with description, name and id to the database. It can also perform updation, reading and deletion activity on the fine-tuned models.

## Methods
- Convert (stream raw_data_request) (stream response_status)      `this will convert raw data to training data`
- GetTrainingData (get_training_data_request) (training_data)     `This will return the final data created`
- AddTrainingData (stream more_raw_data) (stream response_status) `This will convert and append the new raw data to existing training data`
- RemoveTrainingData (remove_request) (response_status)           `This will delete x lines of training data from the file`

## Inputs
- raw_data_request: data_file_name<string>, model_id(optional)<string>, data<string>
- get_training_data_request: data_file_name<string>
- more_raw_data: data_file_name(optional)<string>, model_id(optional)<string>, data_file_id<string>, data<string>
- remove_request: data_file_id<string>

## Output
- response_status: enum
- training_data: data<string>