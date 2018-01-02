(function() {
  (function($) {
    $.widget('IKS.blockquotebutton', {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var buttonQuote, buttonQuoteOut, buttonSet, widget;

        widget = this;
        buttonSet = $('<span class="' + this.widgetName + '"></span>');

        buttonQuote = $('<span></span>');
        buttonQuote.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'Blockquote',
          icon: 'icon-openquote',
          command: null
        });

        buttonQuote.on('click', function(event) {
          widget.options.editable.execute('formatBlock', 'blockquote');
        });
        buttonSet.append(buttonQuote);


        buttonQuoteOut = $('<span></span>');
        buttonQuoteOut.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'Pull Out Quote',
          icon: 'icon-openquote',
          command: null
        });

        buttonQuoteOut.on("click", function(event) {
          var insertionPoint, lastSelection;

          lastSelection = widget.options.editable.getSelection();
          insertionPoint = $(lastSelection.endContainer).parentsUntil('.richtext').last();
          var elem;
          elem = "<blockquote class='pullout'>" + lastSelection + "</blockquote>";

          var node = lastSelection.createContextualFragment(elem);

          lastSelection.deleteContents();
          lastSelection.insertNode(node);

          return widget.options.editable.element.trigger('change');
        });
        buttonSet.append(buttonQuoteOut);

        buttonSet.hallobuttonset();
        toolbar.append(buttonSet);

      }
    });
  })(jQuery);
}).call(this);


(function() {
  (function($) {
    $.widget('IKS.supsubscript', {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var buttonSubscript, buttonSuperscript, buttonSet, widget;

        widget = this;
        buttonSet = buttonSet = $('<span class="' + this.widgetName + '"></span>');

        buttonSuperscript = $('<span></span>');
        buttonSuperscript.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'sup',
          icon: 'icon-arrow-up',
          command: 'superscript'
        });
        buttonSet.append(buttonSuperscript);

        buttonSubscript = $('<span></span>');
        buttonSubscript.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'sub',
          icon: 'icon-arrow-down',
          command: 'subscript'
        });
        buttonSet.append(buttonSubscript);

        buttonSet.hallobuttonset();
        toolbar.append(buttonSet);

        // buttonJustifyRight.on("click", function(event) {
        //   var insertionPoint, lastSelection;
        //
        //   lastSelection = widget.options.editable.getSelection();
        //   insertionPoint = $(lastSelection.endContainer).parentsUntil('.richtext').last();
        //   var elem;
        //   elem = "<p class='text-right'>" + lastSelection + "</p>";
        //
        //   var node = lastSelection.createContextualFragment(elem);
        //
        //   lastSelection.deleteContents();
        //   lastSelection.insertNode(node);
        //
        //   return widget.options.editable.element.trigger('change');
        // });




      }
    });
  })(jQuery);
}).call(this);

// TODO: lolz
(function() {
  (function($) {
    $.widget('IKS.supsubscript', {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var blockHighlightButton, widget;

        widget = this;

        blockHighlightButton = $('<span class="' + this.widgetName + '"></span>');
        blockHighlightButton.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'sup',
          icon: 'icon-arrow-up',
          command: null
        });
        toolbar.append(blockHighlightButton);
        // input
      }

    });
  })(jQuery);
}).call(this);
