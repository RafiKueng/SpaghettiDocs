LMT.events = {
  startUp: function(){
    //...
    LMT.model = new LMT.objects.Model();
    LMT.model.init();
    LMT.events.assignHandlers();
    //...
  },
  
  assignHandlers: function() {
    // ...
    $(document).on('ShowSelectDatasourceDialog',
      LMT.ui.html.SelectDatasourceDialog.show);    

    $(document).on('RepaintModel', LMT.objects.Model.Repaint);

    $(document).on('UploadModel', LMT.com.UploadModel);
    $(document).on('SimulateModel', LMT.events.SimulateModel);

    $(document).on('ReceivedSimulation', LMT.ui.out.load);
    $(document).on('ReceivedSimulation', LMT.ui.html.Toolbar.updateTop);
    // ...
  },
}  
//...