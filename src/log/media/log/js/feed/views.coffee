$ ->
  class AppView extends Backbone.View
    el: '#wrapper'
    
    initialize: (options) ->
      @subviews = [
        #new LogsView collection: @collection
        new NewLogView collection: @collection
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
      try
        values =
          text: @$('#text').val()

        options =
          wait: true
          error: (model, xhr, options) =>
            @showErrors $.parseJSON(xhr.responseText or xhr)['log']
          success: =>
            @render()

        @collection.create values, options
      catch error
        console.log error.message

      false

    showErrors: (errors) ->
      # limpiamos errores previos
      @$('.errorlist').remove()

      for field, error of errors
        errorList = $('<ul/>').addClass 'errorlist'
        errorList.append($('<li/>').text error)
        @$('#' + field).after errorList


  @app = window.app ? {}
  @app.AppView = AppView
