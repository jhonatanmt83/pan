(function($){
    $(function() {
        $('input[data-bootstrap-widget=datepicker]').datepicker({
            onSelect: function(textoFecha, objDatepicker){
                alert('aa');
                //$("#id_fecha").datepicker( "hide" );
            }
        });
    })
})(jQuery);
