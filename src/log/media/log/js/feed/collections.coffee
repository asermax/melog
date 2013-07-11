class Logs extends Backbone.PaginatedCollection
  model: app.Log
  baseUrl: 'api/v1/log'

@app = window.app ? {}
@app.Logs = new Logs
