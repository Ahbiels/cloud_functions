Conseguimos integrar o Cloud build com a Cloud functions, porém, para enviar o código para o cloud build, primeiro é necessário fazer a integração entre uma plataforma externa de versionamento, como o github, com o serviço de **Cloud Source Repository**, para depois enviar para o Cloud Build

<aside>
💡 GitHub → Cloud Source Repository → Cloud Build → Cloud Function
</aside>

O deploy é feito a cada commit no repositório. 

**IMPORTANTE**: Caso haja mais de um path dentro de um repositório, é necessário especifíca-lo na hora de criar o cloud build, assim como especificar a localização do arquivo **cloudbuild.yaml**