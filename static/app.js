$("a[href*='#']").on("click", function(e){
    var anchor = $(this);
    $('html, body').stop().animate({
        scrollTop: $(anchor.attr('href')).offset().top
    }, 777);
    e.preventDefault();

    tweenBlur('.menu', 10, 0);
    $('.menu__container').animate({
    	right : -1000
    },1000);
    $('.menu').fadeOut(1000);

    return false;

});
$(document).ready(function(){
    $("a[href*='#']").on("click", function(e){
    var anchor = $(this);
    $('html, body').stop().animate({
        scrollTop: $(anchor.attr('href')).offset().top
    }, 777);
    e.preventDefault();

    tweenBlur('.menu', 10, 0);
    $('.menu__container').animate({
    	right : -1000
    },1000);
    $('.menu').fadeOut(1000);

    return false;

});
    function mode() {
        var url = $('.getcart').data('url');
        $.ajax({
            url: url,
            success: function(data) {
                $('.left').html(data);
            }
        });
    }; 
    function getsum(){
        var url = $('.getsum').data('url');
        $.ajax({
            url: url,
            success: function(data) {
                $('.basket-icon').attr('data-before', data);
            }
        });
    }
    function priceall() {
        var url = $('.getprice').data('url');
        $.ajax({
            url: url,
            success: function(data) {
                $('.right__offer-sum').html(data);
            }
        });
    }; 
    setInterval(mode, 2000);
    setInterval(priceall, 2000);
    setInterval(getsum, 1000);
    jQuery.fn.outerHTML = function() {
      return jQuery('<div />').append(this.eq(0).clone()).html();
    };
    
    
    
    

    $('form.ajax').on('submit',function(){
        var type = $(this).attr('method');
        var url = $(this).attr('action');
        var data = {};
        // data['answers'] = answers;
        $(this).find('[name]').each(function(index,value){
            var name = $(this).attr('name');
            var val = $(this).val();
            data[name] = val;
        });
        $.ajax({
            url : url,
            type:type,
            data :data,
            success : function(response){
                console.log('сообщение отправленно');
//                tweenBlur('.order', 10, 0);
                $('.order__container').animate({
                    right : -1000
                },1000);
                $('.order').fadeOut(1000);

//                tweenBlur('.menu', 10, 0);
                $('.basket-menu__container').animate({
                    right : -1000
                },500);
                $('.basket-menu').fadeOut(1000);



                $('.sucsess').fadeIn(200);
            }
        });
        return false;
    });
    $('.catalog__item-price-span').each(function() {
      this.innerHTML = (parseInt(this.textContent))
        .toLocaleString('ru-RU')
    })
    $('body').on('click','.form__submit-order',function(){
        console.log('Some check');
        var ht = $('.basket-menu__container').find('.left').outerHTML();
        $('#dataOrder').val(ht);
        console.log(ht);
        
        $('#order-form').submit();

    });
//
//    $('body').on('click','.btn-wrapper',function(){
//        var idd = $(this).data('id');
//        var size = $('.catalog__item#'+idd).find('.center').find('.some_class').text();
//        var data = {};
//        console.log(size);
//        console.log(idd);
//         $.ajax({
//            url : 'addtocart/' + idd + '/' + size + '',
//            type:'GET',
//            data :data,
//            success : function(response){
//                console.log('сообщение отправленно');
//            }
//        });
//    });
//    
    
    
    $('body').on('click','.basket-icon',function(){
        console.log('asdasd');
        $('.basket-menu').css({
            "display":'block'
        });
        // $('.menu').animate({
        //  "backdrop-filter" : 'blur(10px)'
        // },1000);
//        tweenBlur('.basket-menu', 0, 10);
        $('.basket-menu__container').animate({
            right : 0
        },500);
    });

    $('body').on('click','.three',function(){

        // $('.menu').animate({
        //  "backdrop-filter" : 'blur(10px)'
        // },1000);
//        tweenBlur('.menu', 10, 0);
        $('.basket-menu__container').animate({
            right : -1000
        },500);
        $('.basket-menu').fadeOut(1000);
    });
    
    
    
//    $('body').on('click','.item__delete',function(){
//        var data = {}
//        var pk = $(this).attr('id');
//        console.log('asdasd');
//        $.ajax({
//            url : 'delfromcart/' + pk,
//            type:'GET',
//            data :data,
//            success : function(response){
//                console.log('сообщение отправленно');
//            }
//        });
//    });
    
    
    $('body').on('click','.sucsess__container-close',function(){
        $('.sucsess').fadeOut(200);
        console.log('Some click on sucsess')
    });

    
    $('body').on('click','.right__offer',function(){
        console.log('asdasd');
        $('.order').css({
            "display":'block'
        });
//        tweenBlur('.order', 0, 10);
        $('.order__container').animate({
            right : 0
        },1000);
    });


    $('body').on('click','.title__close',function(){

        // $('.menu').animate({
        //  "backdrop-filter" : 'blur(10px)'
        // },1000);
//        tweenBlur('.order', 10, 0);
        $('.order__container').animate({
            right : -1000
        },1000);
        $('.order').fadeOut(1000);
    });

});