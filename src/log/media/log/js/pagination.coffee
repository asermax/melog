class Backbone.PaginatedCollection extends Backbone.Collection
  initialize: ->
    @on 'reset', @setPaginationData, @

  setPaginationData: ->
    @meta.pages = Math.ceil @meta.total_count / @meta.limit
    
  url: ->
    if @meta?
      urlparams =
        offset: @meta.offset
        limit: @meta.limit

      if @meta.order_by
        urlparams.order_by = @meta.order_by

    extra = if urlparams? then '?' + $.param urlparams else ''
    @baseUrl + extra
