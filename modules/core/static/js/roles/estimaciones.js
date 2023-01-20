// bases de ejemplos
/* 
https://jsfiddle.net/vqgo3qga/
http://jsfiddle.net/jakea/42a6c4d4/

*/
// variables
var costo_total = 0;
var bander = false;
var total_fila = 0
var id_bandera = 0;
var bandera_search = false

// cargas rapidas con function
$(function () {
  $('.costos').trigger('onload');
  $('.numero_estimacion').trigger('onload');
  $('.dropdown-concepto').dropdown({
    allowAdditions: true,
    hideAdditions: false,
    message: {
        addResult: 'Agregar: <b>{term}</b>',
    },
});
})

// cargas de clases 
$('.costos').keyup(function (event) {
  $(this).val(function (index, value) {
    return value
      .replace(/\D/g, "")
      .replace(/([0-9])([0-9]{2})$/, '$1.$2')
      .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
  });
});
$('.costos').blur(function () {
  if (!$(this).val() || $(this).val() == 0) {
    $(this).val('0.00')
    $(this).css('color', '#C9C6C6')
    $(this).next().css('color', '#C9C6C6')
    costo_total = 0
      id_bandera = 0
      total_fila = 0
      bander = true
      cargarFilterActualizadoBlur();
  } else {
    costo_total = 0
    id_bandera = 0
    total_fila = 0
    bander = true
    if(!bandera_search) {
      $('.costos').trigger('onload');
    } else {
      cargarFilterActualizadoBlur()
    }
    $(this).css('color', '#77777A')
    $(this).next().css('color', '#77777A')
  }
});

$('.dropdown-estatus').click(function () {
    if ($(this).children()[0].innerText === 'En proceso') {
    $($(this).parent().parent()[0].cells[0]).css({
      'border-left': '3px  #FE0919 solid',
      'width': '9%'
    })
    $($(this).children()[0]).css({
      'color': '#FE0919'
    })
  } else if ($(this).children()[0].innerText === 'Facturada' || $(this).children()[0].innerText === 'Cobrada') {
    $($(this).parent().parent()[0].cells[0]).css({
      'border-left': '3px  #00CF61 solid',
      'width': '9%'
    })
    $($(this).children()[0]).css({
      'color': '#00CF61'
    })
  } else {
    $($(this).parent().parent()[0].cells[0]).css({
      'border-left': '3px  #FFC600 solid',
      'width': '9%'
    })
    $($(this).children()[0]).css({
      'color': '#FFC600'
    })
  }
});

$('.numero_estimacion').keyup(function(){
  $(this).val(function(index, value) {
    return value.replace(/\D/g, "")
  })
})


$('.numero_estimacion').blur(function(){
  if(!$(this).val() || $(this).val() == 0 ) {
    $(this).val('S/N');
    $(this).css('color', '#C9C6C6');
    costo_total = 0
    bander = true;
    $('.costos').trigger('onload');
  } else  {
    $(this).css('color', '#77777A')
    costo_total = 0
    bander = true;
    $('.costos').trigger('onload');
  } 
  
});

$('.calendar_tramite').click(function() {
  var fecha = new Date();
  var label_fecha  = fecha.toISOString().substring(0, 10); 
  $(this).val(label_fecha)
});

$('.iva_check').click(function () {
  costo_total = 0;
  id_bandera = 0;
  total_fila = 0;
  bander = true;
  if(!bandera_search) {
    $('.costos').trigger('onload');
  } else {
    cargarFilterActualizadoBlur()
  }
});

$('#search').click(function () {
  var txtValue
  var search = $('#input_search').val().toUpperCase();
  var filas = $('.filas-search tr')

  for (let i = 0; i < filas.length; i++) {
    var td = filas[i].getElementsByTagName('td')[0];
    if (td) {
      txtValue = td.textContent || td.innerText;

      if (txtValue.toUpperCase().indexOf(search) > -1) {
        filas[i].style.display = "";
      } else {
        filas[i].style.display = "none";
      }
    }
  }
});
$('#filter_estatus').dropdown({
  onChange: function (value, text, $selectedItem) {
    var valor = '(' + text + ')'
    $('#estatus_text').text(valor)
    if (value == 'todos') {
      var filas = $('.filas-search tr')
      for(let i = 0; i < filas.length; i++) {
        filas[i].style.display = "";
      }
      costo_total = 0
      id_bandera = 0
      total_fila = 0
      bander = true
      $('.costos').trigger('onload');
      bandera_search =  false
    } else {
      search_table(text.toUpperCase());
      bandera_search = true
    }
  }
});


// ---------------------------------------------------------------------------------------------------------------------------------------------

// --------------------------------------- Funciones --------------------------------------------- 
// validacion de numeros si existe o no
function LoadNumero(event) {
  if(event.val() == 'S/N' || event.val() == 0) {
    event.val('S/N');
    event.css('color', '#C9C6C6');
  } else {
    event.css('color', '#77777A')
  }
};
// validacion de costo y hace el calculo
function LoadCosto(event, id) {
  
  if ($("#n_id_" + id).val() == 'S/N' || $("#n_id_" + id).val() == 0 || !$("#iva_check_" + id).is(':checked') ) {
    CalcularSinIva(event, id);
    
  } else {
    CalcularConIva(event, id);
    
  }
};

// funcion calculo linea por linea
function total_linea(valor, id) {
  if (id == id_bandera) {
    
    var iva =  parseFloat(valor) * 0.16
    var iva_conver = ReplaceNumberWithCommas(iva)
    total_fila += parseFloat(valor) * 1.16
    total_fila_conver = ReplaceNumberWithCommas(total_fila)
    $('#costo_lineal_' + id).val(total_fila_conver)
    $('#iva_val_' + id).val(iva_conver)
    $('#iva_val_' + id).css('color', '#77777A')
    $('#iva_val_' + id).next().css('color', '#77777A')

  } else {
    id_bandera = id
    total_fila = 0
    total_linea(valor, id)
  }
};
// funcion calculo linea sin iva 
function total_linea_sin_iva(valor, id) {
  if (id == id_bandera) {
    total_fila += parseFloat(valor)
    total_fila_conver = ReplaceNumberWithCommas(total_fila)
    $('#costo_lineal_' + id).val(total_fila_conver)
    $('#iva_val_' + id).val('0.00')
    $('#iva_val_' + id).css('color', '#77777A')
    $('#iva_val_' + id).next().css('color', '#77777A')

  } else {
    id_bandera = id 
    total_fila = 0
    total_linea_sin_iva(valor, id)
  }
}
// funcion que remplaza las comas y devuleve el resulto para trabajar 
function ReplaceNumberWithCommas(yourNumber) {
  //separa el componente por el punto
  // var n = yourNumber.toString().split(".");
  var n = Math.round(yourNumber).toString()
  
  //agrega la coma ala primera parte
  // n[0] = n[0].replace(/([0-9])([0-9]{2})$/, '$1.$2').replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  var numero_return = n.concat('00') 
  //combina de nuevo
  // return n.join(".");
  return numero_return.replace(/([0-9])([0-9]{2})$/, '$1.$2').replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};
function search_table(filter) {
  var txtValue
  total_fila = 0 
  costo_total = 0
  var search = filter
  var filas = $('.filas-search tr')

  for(let i = 0; i < filas.length; i++) {
    var td  =  filas[i].getElementsByTagName('td')[6].getElementsByTagName('div')[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(search) > -1) {
        calcularFilter(filas[i].dataset.estimaciones);
        filas[i].style.display = "";
      } else {
        filas[i].style.display = "none"
      }
    }
  }
  total(costo_total);
};
function cargarFilterActualizadoBlur() {
  var filas = $('.filas-search tr')
  
  $(filas).each(function () {
    if($(this).css("display") == 'table-row') {
      calcularFilter($(this).data('estimaciones'))
    }
  });
  total(costo_total);
};
function calcularFilter(filas) {
  var fila_tds =  $('.filas-search tr[data-estimaciones='+ filas +']').children()
  var presupuesto = parseFloat(fila_tds.children().children()[6].value.replace(/,/g, ""))
  if($("#iva_check_" + filas).is(':checked')) {
    var total_row =  presupuesto * 1.16
    costo_total += total_row
    var total_linea_conversion = ReplaceNumberWithCommas(total_row)
    var iva = presupuesto * 0.16
    var conversion_iva = ReplaceNumberWithCommas(iva)
    $('#costo_lineal_' + filas).val(total_linea_conversion)
    $('#iva_val_' +  filas).val(conversion_iva)
    } else {
    costo_total += presupuesto
    var total_linea_conversion_sin_iva = ReplaceNumberWithCommas(presupuesto)
    $('#costo_lineal_' + filas).val(total_linea_conversion_sin_iva)
    $('#iva_val_' +  filas).val('0.00')
  }
};
// funcion para el valor string con comas a cantidad entera base blur, y actualizacion
function pasarStringAInt(data, id) {
  var ejemplo = data.replace(/,/g, "")
  costo_total += parseFloat(ejemplo * 1.16)
  total_linea(ejemplo, id)
  total(costo_total);
};
function pasarStringAIntSinIva(data, id) {
  var ejemplo = data.replace(/,/g, "")
  costo_total += parseFloat(ejemplo)
  total_linea_sin_iva(ejemplo, id)
  total(costo_total);
};
// calculo total 
function total(precio) {
  x = ReplaceNumberWithCommas(precio)
  $('#costoTotal').val(x)
};
// funcion para calcular sin iva
function CalcularSinIva(event, id) {
  
  if (!bander) {
    if (event.val() == 0) {
      event.val('0.00')
      event.css('color', '#C9C6C6');
      event.next().css('color', '#C9C6C6');
    } else {
      costo_total += parseInt(event.val())
      event.css('color', '#77777A');
      event.next().css('color', '#77777A');
      event.val(function (index, value) {
        return value
          .replace(/\D/g, "")
          .replace(/([0-9])([0-9]{2})$/, '$1.$2')
          .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
      });
      total_linea_sin_iva(event.val().replace(/,/g, ""), id)
      total(costo_total)
    }
  } else {
    pasarStringAIntSinIva(event.val(), id)
  }
};
// funcion para calcular con iva 
function CalcularConIva(event, id) {
  if (!bander) {
    if (event.val() == 0) {
      event.val('0.00')
      event.css('color', '#C9C6C6');
      event.next().css('color', '#C9C6C6');
    } else {
      costo_total += parseInt(event.val() * 1.16)
      event.css('color', '#77777A');
      event.next().css('color', '#77777A');
      event.val(function (index, value) {
        return value
          .replace(/\D/g, "")
          .replace(/([0-9])([0-9]{2})$/, '$1.$2')
          .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
      });
      total_linea(event.val().replace(/,/g, ""), id)
      total(costo_total);
    }
  } else {
    pasarStringAInt(event.val(), id)
  }
};
// funcion para recorrer la tabla y buscar el numero maximo 
function MaxNumberTable() {
  var mayor = 0
  filas = $('#table-estimaciones > tr').toArray()
  $.each(filas, function(index, data){
    valor = $(this).children('td').children('.ui.fluid.transparent.input').children('.numero_estimacion').val()
    if ( parseInt(valor) > mayor ) {
      mayor = parseInt(valor)
    }
  })
  return mayor + 1
}
// funcion para agregar un tr en la tabla
function agregarFila() {
  var fecha = new Date();
  var label_fecha  = fecha.toISOString().substring(0, 10); 
  // var id =  Date.parse(fecha);
  var id = MaxNumberTable(); 
  // console.log(id)
  var Fila = `
  <tr style="color: #77777A; font-size: 14px;" data-estimaciones="${id}">
  <td style="border-left: 3px  #FE0919 solid; width: 9%;">
    <div class="ui fluid transparent  input">
      <input id="n_id_${id}" type="text" class="numero_estimacion" onload="LoadNumero($(this))" value="${id}" readonly>
    </div>
  </td>
  <td style="width: 7%; padding-left: 0 !important;">
    <div class="ui  left icon transparent input">
      <input class="calendar_tramite" type="date" value="${label_fecha}" onload="LoadCalendar($(this))" style="color: #77777A; padding-left: 17px !important;" >
      <i class="calendar icon icon-tramitologia" style="font-size: 14px !important;"></i>
    </div>
  </td>
  <td style="width: 23%; ">
    <div class="ui fluid search selection dropdown dropdown-concepto">
      <i class="dropdown icon"></i>
      <div class="default text">Skills</div>
      <div class="menu">
        <div class="ui icon search input">
          <i class="search icon"></i>
          <input type="text" placeholder="Search tags...">
        </div>
        <div class="item" data-value="angular">Angular</div>
        <div class="item" data-value="css">CSS</div>
        <div class="item" data-value="css">Java</div>
        <div class="item" data-value="css">Jquery</div>
        <div class="item" data-value="css">Python</div>
      </div>
     
    </div>
  </td>
  <td style="width: 14%;">
    <div class="ui fluid left icon transparent input">
      <input type="text" onload="LoadCosto($(this), '${id}')" class="costos" value="0.00"
        style="padding-left: 17px !important;">
      <i class="dollar sign icon" style="font-size: 14px !important;"></i>
    </div>
  </td>
  <td style="width: 15%;">
    <div class="ui fluid left icon transparent input">
      <input type="text" readonly id="iva_val_${id}"
        style="padding-left: 17px !important;">
      <i class="dollar sign icon" style="font-size: 14px !important;"></i>
      <div class="ui checkbox">
            <input class="iva_check" id="iva_check_${id}" type="checkbox" checked>
            <label></label>
          </div>
    </div>
  </td>
  <td style="width: 13%;">
    <div class="ui fluid left icon transparent input">
      <input type="text" class="costo_total" id="costo_lineal_${id}" value="0.00" style="padding-left: 17px !important;"
        readonly>
      <i class="dollar sign icon" style="font-size: 14px !important;"></i>
    </div>
  </td>
  <td style=" width: 9%;padding-left: 0 !important;padding-right: 0 !important;" class="center aligned">
    <div class="ui inline   dropdown dropdown-estatus">
      <div class="text" style="color: #FE0919;" id="estatus_text_1">
      En proceso
      </div>
      <i class="dropdown icon"></i>
      <div class="menu">
        <div class="item" style="color: #00CF61;">
          Facturada
        </div>
        <div class="item" style="color: #00CF61;">
              Cobrada
        </div>
        <div class="item" style="color: #FFC600;">
          Aprobada
        </div>
        <div class="item" style="color: #FE0919;">
          En proceso
        </div>
      </div>
    </div>
  </td>
  <td style=" width: 5%;" class="center aligned"><i class="file alternate outline icon icon-tramitologia"></i></td>
  <td style=" width: 5%;" class="center aligned"><i class="trash icon icon-tramitologia"></i></td>
</tr>
  `
  costo_total = 0;
  id_bandera = 0;
  total_fila = 0
  bander=true

  $(Fila).appendTo('#table-estimaciones');
  // $('.costos').trigger('onload');
  if(!bandera_search) {
    $('.costos').trigger('onload');
  } else {
    cargarFilterActualizadoBlur()
  }
  $('.numero_estimacion').trigger('onload');
  $('.ui.inline.dropdown').dropdown();
  $('.dropdown-concepto').dropdown({
    allowAdditions: true,
    hideAdditions: false,
    message: {
        addResult: 'Agregar: <b>{term}</b>',
    },
  });
  // cargas de clases 
  $('.costos').keyup(function (event) {
    $(this).val(function (index, value) {
      return value
        .replace(/\D/g, "")
        .replace(/([0-9])([0-9]{2})$/, '$1.$2')
        .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
    });
  });
  $('.costos').blur(function () {
    if (!$(this).val() || $(this).val() == 0) {
      $(this).val('0.00')
      $(this).css('color', '#C9C6C6')
      $(this).next().css('color', '#C9C6C6')
      costo_total = 0
        id_bandera = 0
        total_fila = 0
        bander = true
        cargarFilterActualizadoBlur();
    } else {
      costo_total = 0
      id_bandera = 0
      total_fila = 0
      bander = true
      if(!bandera_search) {
        $('.costos').trigger('onload');
      } else {
        cargarFilterActualizadoBlur()
      }
      $(this).css('color', '#77777A')
      $(this).next().css('color', '#77777A')
    }
  });
  
  $('.dropdown-estatus').click(function () {
      if ($(this).children()[0].innerText === 'En proceso') {
      $($(this).parent().parent()[0].cells[0]).css({
        'border-left': '3px  #FE0919 solid',
        'width': '9%'
      })
      $($(this).children()[0]).css({
        'color': '#FE0919'
      })
    } else if ($(this).children()[0].innerText === 'Facturada' || $(this).children()[0].innerText === 'Cobrada') {
      $($(this).parent().parent()[0].cells[0]).css({
        'border-left': '3px  #00CF61 solid',
        'width': '9%'
      })
      $($(this).children()[0]).css({
        'color': '#00CF61'
      })
    } else {
      $($(this).parent().parent()[0].cells[0]).css({
        'border-left': '3px  #FFC600 solid',
        'width': '9%'
      })
      $($(this).children()[0]).css({
        'color': '#FFC600'
      })
    }
  });
  
  $('.numero_estimacion').keyup(function(){
    $(this).val(function(index, value) {
      return value.replace(/\D/g, "")
    })
  })
  
  
  $('.numero_estimacion').blur(function(){
    if(!$(this).val() || $(this).val() == 0 ) {
      $(this).val('S/N');
      $(this).css('color', '#C9C6C6');
      costo_total = 0
      bander = true;
      $('.costos').trigger('onload');
    } else  {
      $(this).css('color', '#77777A')
      costo_total = 0
      bander = true;
      $('.costos').trigger('onload');
    } 
    
  });
  
  $('.calendar_tramite').click(function() {
    var fecha = new Date();
    var label_fecha  = fecha.toISOString().substring(0, 10); 
    $(this).val(label_fecha)
  });
  
  $('.iva_check').click(function () {
    costo_total = 0;
    id_bandera = 0;
    total_fila = 0;
    bander = true;
    if(!bandera_search) {
      $('.costos').trigger('onload');
    } else {
      cargarFilterActualizadoBlur()
    }
  });
  
  $('#search').click(function () {
    var txtValue
    var search = $('#input_search').val().toUpperCase();
    var filas = $('.filas-search tr')
  
    for (let i = 0; i < filas.length; i++) {
      var td = filas[i].getElementsByTagName('td')[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
  
        if (txtValue.toUpperCase().indexOf(search) > -1) {
          filas[i].style.display = "";
        } else {
          filas[i].style.display = "none";
        }
      }
    }
  });
  $('#filter_estatus').dropdown({
    onChange: function (value, text, $selectedItem) {
      var valor = '(' + text + ')'
      $('#estatus_text').text(valor)
      if (value == 'todos') {
        var filas = $('.filas-search tr')
        for(let i = 0; i < filas.length; i++) {
          filas[i].style.display = "";
        }
        costo_total = 0
        id_bandera = 0
        total_fila = 0
        bander = true
        $('.costos').trigger('onload');
        bandera_search =  false
      } else {
        search_table(text.toUpperCase());
        bandera_search = true
      }
    }
  });
  
}

// ---------------------------------------------------------------------------------------------