@app = window.app ? {}

$ ->
    Backbone.Tastypie.csrfToken = $('meta[name="csrf-token"]').attr('content')

    new app.AppView collection: app.Logs
    app.Logs.fetch reset: true
         
    
