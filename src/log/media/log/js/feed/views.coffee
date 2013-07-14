$ ->
  class AppView extends Backbone.View
    el: '#wrapper'
    
    initialize: (options) ->
      @subviews = [
        new NewLogView collection: @collection
        new LogsView collection: @collection
      ]
      @collection.bind 'reset', @render, @

    render: ->
      @$el.empty()
      @$el.append view.render().el for view in @subviews
      @


  class NewLogView extends Backbone.View
    tagName: 'form'
    template: _.template $('#new_log_view_template').html()
    events:
      'submit': 'submit'
      'keypress #text': 'submitOnEnter'
    
    render: ->
      @$el.html @template()
      @

    submitOnEnter: (event) ->
      if event.keyCode is 13 and event.shiftKey is false
        event.preventDefault()
        @submit()

    submit: ->
      values =
        text: @$('#text').val()

      log = new Log values, collection: @collection

      if not log.save(null, error: @parseErrors)
        @showErrors log, log.validationError

      # return false to prevent the default behaviour
      false

    addLog: (model) ->
      @collection.add model, at: 0

      # clean errors and regain focus on the text area
      @cleanErrors()
      @focus()

    parseErrors: (model, xhr) =>
      @showErrors model, $.parseJSON(xhr.responseText or xhr)['log']

    cleanErrors: ->
      @$('.errorlist').remove()

    showErrors: (model, errors) ->
      for field, error of errors
        errorList = $('<ul/>').addClass 'errorlist'
        errorList.append($('<li/>').text error)
        @$('#' + field).after errorList

    focus: ->
      @$('#text').val('').focus()


  class LogView extends Backbone.View
    className: 'log'
    tagName: 'div'
    template: _.template $('#log_view_template').html()
    
    render: ->
      @$el.html @template(@model.toJSON())
      @

  class LogsView extends Backbone.View
    id: 'logs'
    tagName: 'div'
    
    initialize: (options) ->
      @collection.bind 'add', @render, @

    render: ->
      @$el.empty()

      for log in @collection.models
        logView = new LogView model: log
        @$el.append logView.render().el

      @

  @app = window.app ? {}
  @app.AppView = AppView
