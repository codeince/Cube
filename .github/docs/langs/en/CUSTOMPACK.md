# YOUR OWN Cube

If you need to create your own Cube, maybe with swearing or humorer answers, this documentation was created just for you

After creating of resource-pack you need to change value of variable in the `src/__main__.py` file in line **resource_pack = 'resource-pack name'**

# Resource-pack Structure

Your resource-pack must include this files:

1. Language(`/langs/language.json`): main Cube actions writes right here
2. Answer(`/langs/answer_files/answers_language.json`): Cube's dictionary for Cube's reactions writes right here

# Language File

For now this file has so pure settings but included settings are:

1. "lang": language of file

2. "text": displayed text settings:

    1. "init_text": text writes when model starts

    2. "answer_formatting": text formatting

        {answer} - answer

        {question}" - user question

    3. "type_text": question input text

    4. "model_text": text formatting of Model

        {seed} - current "identity"

    5. "custom_model_text": text formatting for choosing model seed

    6. "stop_words": list of words for Cube stopping

    7. "war_and_piece_warning": text will show when user question equal or more than "war_and_piece_warning_len"

# Answer file

In this file logically too many different settings... groups:

1. "lang": language of file

2. "answers": list of answer groups

    "test answer group": answer group

        1. "masks": piece of text in user question for determination of current group(first mask should be "#group_name")

        2. "answers": answers for group questions
        
            %rand% for generation random number here

# And keep in mind

If you don't understood you need just send me your problem
