

 $(document).ready(function() {
        $('body').ihavecookies({
            title: '&#x1F36A; Aceptar cookies y política de privacidad?',
            message: 'No se utilizan cookies en este sitio, pero si las hubiera, este mensaje podría personalizarse para proporcionar más detalles. Haga clic en el botón <strong>aceptar</strong> a continuación para ver la devolución de llamada opcional en acción ...',
            delay: 600,
            expires: 1,
            link: '#privacy',
            onAccept: function(){
                var myPreferences = $.fn.ihavecookies.cookie();
                console.log('¡SI! Se guardaron las siguientes preferencias...');
                console.log(myPreferences);
            },
            uncheckBoxes: true,
            acceptBtnLabel: 'Aceptar',
            moreInfoLabel: 'Más información'
        });

        if ($.fn.ihavecookies.preference('marketing') === true) {
            console.log('Para Marketing.');
        }
    });