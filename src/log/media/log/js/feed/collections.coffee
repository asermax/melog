class Logs extends Backbone.PaginatedCollection
  model: app.Log
  urlRoot: 'api/v1/log'

@app = window.app ? {}
@app.Logs = new Logs
