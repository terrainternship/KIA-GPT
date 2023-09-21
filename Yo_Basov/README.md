Tutorial: https://goo.su/Anp6
PDF: https://goo.su/uirUv4n
Habr: https://habr.com/ru/articles/717816/
Example: https://github.com/ViktorAllayarov/ChatGPT_telegram_bot
Article: https://code.visualstudio.com/docs/containers/ssh
Hosting: https://console.cloud.yandex.com

![Screenshot_1](https://github.com/terrainternship/KIA-GPT/assets/29410375/5e71b38c-86d6-448f-a5db-f7635930313e)

`CRAZY API SCHEME`

`**********************************************************************************************************************`

`   <----------------------------------------------------------------|`

`TG  BOT          API                                                API                  API                TG BOT`

`         --->           -------------> PARSER ---------------->             --------->          <----------`

` ADMIN         BUILDER                                           ASSEMBLER  <--------- CHATBOT  ----------> CLIENT`

`   |              |                                                 ^ ^ ^                 |     ^              V ^ `

`   |              |                                                 | | |                 V     |--------------| | `

`   |              |                                                 | | |               IMAGE                MODEL `

`   |              |------------------> PDF PARSER ------------------| | |                         <-----|          `

`   |                                                                  | |               READER       |--|   LOGGER`

`   |              API                                                 | |                 |          |         ^`

`   |-------->          --------------> WHISPER ---------------------- | |                 V          |         |`

`                 VIDEO                                                    |              AUDIO    <--|       DIALOG`

`                   |                                                      |                       ------>`

`                   |------------------> YOLO    --------------------------|             LISTENER              SEARCH`

`**********************************************************************************************************************`

`swagger.io`

`api builder`

`Everything about api builder`

``

`POST`

`/builder/{builderId}/process`

`process admin tg bot command`

`Parameters`

`Try it out`

`Name	Description`

`builderId *`

`integer($int64)`

`ID of builder to update`

`builderId`

`additionalMetadata`

`string`

`(formData)`

`Additional data to pass to server`

`additionalMetadata`

`file`

`file`

`(formData)`

`file to upload`

`Файл не выбран`

`Responses`

`Response content type`

`application/json`

`Code	Description`

`200	`

`successful operation`

`Example Value`

`Model`

`{`

`  "code": 0,`

`  "type": "string",`

`  "message": "string"`

`}`
