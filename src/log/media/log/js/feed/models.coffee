class Log extends Backbone.Model
  validate: (attributes) ->
    merged = _.extend _.clone(@attributes), attributes
    errors = {}

    if not merged.text or merged.text.trim() is ''
      errors['text'] = "The log can't be empty"

    errors unless _(errors).isEmpty()


@app = window.app ? {}
@app.Log = Log
