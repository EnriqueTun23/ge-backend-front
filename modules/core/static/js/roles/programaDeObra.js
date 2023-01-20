// cargar elementos 
var bander = false;
var costo_total = 0;

var totalGeneral = 0;
var totalModulos = 0;
var totalIvas = 0;

var moduloJSON = {
  "result": [
    {"title": "Andenes 1,2 Y puerta 1"},
    {"title": "Puerta 1"},
    {"title": "Cerrajeros Y Puerta 1"},
    {"title": "Bobedillas"},
    {"title": "Andenes"},
    {"title": "Aandenes Y Cerraduras"}
  ]
}

// id para ocultar
$('#text-modulo').hide();
$('#button-module').hide();

$(function() {
    LoadClass();
});

// Esta es una funcion que carga todas las clases necesarias
LoadClass = (e) => {
    $('.costos').trigger('onload');
    $('.date_range').trigger('onload');
    $('.modulo_total').trigger('onload')
    $('.date_range').daterangepicker({
        locale: {
            format: 'DD/MM/YYYY'
        }
    });    
    $('.date_range').on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
        LoadCalendar($(this))
    });
  
    $('.date_range').on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    });

    $('.progress_cronograma').progress()
    $('.dropdown-estatus').click(function () {
        if ($(this).children()[0].innerText === 'Urgente') {
        $($(this).parent().parent()[0].cells[0]).css({
          'border-left': '3px  #FE0919 solid',
        })
        $($(this).children()[0]).css({
          'color': '#FE0919'
        })
      } else if ($(this).children()[0].innerText === 'Media') {
        $($(this).parent().parent()[0].cells[0]).css({
          'border-left': '3px  #00CF61 solid',
        })
        $($(this).children()[0]).css({
          'color': '#00CF61'
        })
      } else if ($(this).children()[0].innerText === 'Alta') {
        $($(this).parent().parent()[0].cells[0]).css({
          'border-left': '3px  #FF8C00 solid',
        })
        $($(this).children()[0]).css({
          'color': '#FF8C00'
        })
      } else {
        $($(this).parent().parent()[0].cells[0]).css({
          'border-left': '3px  #FFC600 solid',
        })
        $($(this).children()[0]).css({
          'color': '#FFC600'
        })
      }
    });
    
    $("table tbody").sortable({
      handle: '.arrows',
      axis: 'y',
      cancel: ''
    }).disableSelection();
    calculerPorcentaje();
    // setTimeout(calculerPorcentaje, 1500);
}

// cargar costo
LoadCosto = (e, id, select) => {
    
    FilterValue(e, select);
}

// Blur calendar
BluerCalendar = e => {
  LoadCalendar(e);
}
// Blur cargar total del valor si alcanza
calculoTotalModule = (e) => {
  totalGeneral = 0;
  totalModulos = 0;
  totalIvas = 0;
  calculerPorcentaje();
}

// keypress para poner el valor con comas y dos puntos 
 convertTextToMoney = (e) => {
  if (e.val() == 0){
    e.val('0.00');
    e.css('color', '#C9C6C6');
    e.next().css('color', '#C9C6C6');
  } else {
    e.css('color', '#77777A');
    e.next().css('color', '#77777A');
    e.val((index, value) => {
      return value
      .replace(/\D/g, "")
      .replace(/([0-9])([0-9]{2})$/, '$1.$2')
      .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
    })
  }
}
 
// LoadTotal
totalModule = (eve) => {
  if(eve.val() == 0) {
    eve.val('0.00');
    eve.css('color', '#C9C6C6');
    eve.next().css('color', '#C9C6C6');  
} else {
    eve.css('color', '#77777A');
    eve.next().css('color', '#77777A');
    eve.val((index, value) => {
        return value
        .replace(/\D/g, "")
        .replace(/([0-9])([0-9]{2})$/, '$1.$2')
        .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
    });
}
}

// cargar  calendario 
LoadCalendar = (e) => {
    let fechas = e.val().split("-")
    let StartSplit =  fechas[0].split("/")
    let EndSplit =   fechas[1].split("/")
    let startDate = moment(new Date (StartSplit[2],StartSplit[1]-1,StartSplit[0]));
    let EndDate = moment(new Date (EndSplit[2],EndSplit[1]-1,EndSplit[0]));
    let today = moment();
    
    let parcentData = CalculoDeDiffDays(startDate, EndDate, today);
       
    $(e.parents('tr').children('td').children('.ui.indicating.fluid.progress')).progress({percent: parcentData})
}

// cargar lista de modulos 
LoadModulo = (e) => {
  $.each(moduloJSON.result, (key, valor) => {
    var list = ` 
    <div class="fields fields-list">  
    <div class=" fifteen wide field" style="margin-bottom: 8px; cursor:pointer;">
        <div class="ui checkbox checkbox_module">
          <input class="checkbox_module_che" type="checkbox" id="check_module_${valor.key}">
          <label for="check_module_${key}" style="padding-left: 40px; color:#77777A; cursor:pointer; font-weight: normal;">${valor.title} </label>
        </div>
    </div> 
  </div> 
    `
  $(list).appendTo('#list_modulo');
  // ClickCheckbox();
})
} 


ClickCheckbox = (e) => {
  $('.checkbox_module_che').click( function() {
    if($(this).is(':checked')){ $(this).next('label').css({'color' : '#FFC600', 'font-weight': 'bold'})} else { $(this).next('label').css({'color' : '#77777A', 'font-weight' : 'normal'}) }
  })
} 

// filtrar el valor si tiene 0 o no
FilterValue = (e, select_id) => {
    if(!bander) {
        if(e.val() == 0) {
            e.val('0.00');
            e.css('color', '#C9C6C6');
            e.next().css('color', '#C9C6C6');  
        } else {
            e.css('color', '#77777A');
            e.next().css('color', '#77777A');
            e.val((index, value) => {
                return value
                .replace(/\D/g, "")
                .replace(/([0-9])([0-9]{2})$/, '$1.$2')
                .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ",");
            });
        }
    } else {
      pasarStringAInt(e.val(), select_id)
    }
}
function pasarStringAInt(data, select_id) {
  var data_convertido = data.replace(/,/g, "")
  costo_total += parseFloat(data_convertido * 1.16)
  $('#'+select_id).val(ReplaceNumberWithCommas(costo_total))
};



// agregar modulo 
addModuloItem = (e) => {
  var newModule = $('#input_search_modulo').val()
  var fecha = new Date();
  var id = Date.parse(fecha);
  var item = `
  <div class="fields fields-list">  
  <div class=" fifteen wide field" style="margin-bottom: 8px; cursor:pointer;">
      <div class="ui checkbox checkbox_module">
        <input class="checkbox_module_che" type="checkbox" id="check_module_${id}" checked>
        <label for="check_module_${id}" style="padding-left: 40px; color:#77777A; cursor:pointer; font-weight: normal;">${newModule} </label>
      </div>
  </div> 
</div> 
  `
  $('#text-modulo').hide();
    $('#button-module').hide();
    $('#id_ok_modulo').show();
    $('#list_modulo').show();
    $('#list_modulo').html('');
    $(item).appendTo('#list_modulo');
    $.when(LoadModulo()).then(() => {
      moduloJSON.result.push({"title": newModule})
    });

}
// remplaza el el numero a string y lo convierte 
ReplaceNumberWithCommas = (valueNumber) => {
    var n = Math.round(valueNumber).toString();
    var numero_return = n.concat('00')
    return numero_return.replace(/([0-9])([0-9]{2})$/, '$1.$2').replace(/\B(?=(\d{3})+(?!\d))/g, ",")

}
// calcular diferencias de Dias
CalculoDeDiffDays = (start, end, today) => {
   let totalDays = end.diff(start, 'days');
   let DaysBeforeFinish =  end.diff(today, 'days');
   let DaysElapsed = today.diff(start, 'days');

  if (DaysBeforeFinish > 0) {
    let porcentaje = totalDays/100
    return trunc((DaysElapsed/porcentaje), 2)
  } else {
    return 100
  }
}

// porcentajes
totalPorcentaje = (id, total) =>  {
 let totalValue = total
 let totalValuePorcentaje =  total/100
 filas = $('#' + id + '> tr').toArray();
 $.each(filas, function()  {
     let valorDeNumeroConiva = parseFloat($(this).children('td').children('.numeros').children('.costos').val().replace(/,/g, ""))
     totalModulos += valorDeNumeroConiva
     totalIvas += valorDeNumeroConiva * 0.16
     totalGeneral += valorDeNumeroConiva + valorDeNumeroConiva * 0.16
      
     $('#totalSub').text('$' + ReplaceNumberWithCommas(totalModulos))
      $('#totalIVA').text('$' + ReplaceNumberWithCommas(totalIvas))
      $('#totalGeneral').text('$' + ReplaceNumberWithCommas(totalGeneral))
     totalValue = totalValue - valorDeNumeroConiva
     if (totalValue > 0) {
        let valor_porcentage =  trunc((valorDeNumeroConiva/totalValuePorcentaje), 2)
        $(this).children('td').children('.porcentajeDiv').children('.porcentajeInput').val(valor_porcentage)
        $(this).children('td').children('.numeros').addClass('transparent').removeClass('error') 
      } else {
        $(this).children('td').children('.numeros').addClass('error').removeClass('transparent') 
        
      }
 })
}

// truncar a 2 posiones el el porcentaje
function trunc (x, posiciones = 0) {
  var s = x.toString()
  var l = s.length
  var decimalLength = s.indexOf('.') + 1
  var numStr = s.substr(0, decimalLength + posiciones)
  return Number(numStr)
}
// agregar nueva tabla de modulo
addModule = (e) => {
  let checks =  $('.checkbox_module')
  $.each(checks, (index, value) => {
      var tablesTotales = $('#container-desktop > table').toArray().length
      if ($(value).children('.checkbox_module_che').is(':checked')) {
              var name =  $(value).children('label').text()
              htmlTableModule(name, tablesTotales += 1);
      }
  })
}

// abrir modal del modulo click
modal_modulo = () => {
  $('#modal_modulo').modal({ closable: false }).modal('show');
  $('#list_modulo').html('')
  $('#input_search_modulo').val('')
  LoadModulo();
}

// abrir modal de un modulo para agregar fila
modal_fila = (bodyTable, TotalTable ) => {
  htmlFilaTableModule(bodyTable, TotalTable)
}

// for calculo porcentaje
calculerPorcentaje = (e) => {
 let valores =  $('.modulo_total')
 $.each(valores, (index, value) => {
  let id_variable =  $(value).parent().parent().parent().parent().parent().children('tbody').attr('id')
  let total = $(value).val().replace(/,/g, "")
    totalPorcentaje(id_variable, parseFloat(total))
  })
}

// search module 

search_modulo = (e) => {
 
  var search = e.val().toUpperCase();
  $('#text-cambiante').text(e.val());
  if (search.length > 0) {
    var result_filter = $(moduloJSON.result).filter((i, n) => { return !n.title.toUpperCase().indexOf(search)});
    $('#list_modulo').show();
    if(result_filter.length > 0) {
      $('#button-module').hide();
      $('#text-modulo').hide();
      $('#id_ok_modulo').show();
      $('#list_modulo').html('');
      $.each(result_filter, (key, valor) => {
        var list = ` 
          <div class="fields fields-list">  
            <div class=" fifteen wide field" style="margin-bottom: 8px; cursor:pointer;">
              <div class="ui checkbox checkbox_module">
                <input class="checkbox_module_che" type="checkbox" id="check_module_${key}">
                <label for="check_module_${key}"  style="padding-left: 40px; color:#77777A; cursor:pointer; font-weight: normal;">${valor.title} </label>
              </div>
            </div> 
          </div> 
      ` 
      $(list).appendTo('#list_modulo');
      // ClickCheckbox();
      })
    } else {
      $('#text-modulo').show();
      $('#button-module').show();
      $('#id_ok_modulo').hide();
      $('#list_modulo').hide();
    }

  } else {
    $('#text-modulo').hide();
    $('#button-module').hide();
    $('#id_ok_modulo').show();
    $('#list_modulo').show()
    $('#list_modulo').html('')
    LoadModulo();
  }
  let palabraConvertida = e.val().charAt(0).toUpperCase() + e.val().slice(1)
  e.val(palabraConvertida)
}
// contar tablas hasta el momento
countTable = e  => {
   var tablesTotales = $('#container-desktop > table').toArray()
  return tablesTotales.length + 1 
  
}

// onclick Eliminar el contenido
deleteValInput = (e) => {
  e.val('')
}


// html table module 

htmlTableModule = (name, numModule) => {
  var nameNoSpaces = name.replace(/ /g, "")
  let today = moment().format('DD/MM/YYYY');
  let twoDays = moment().add('days', 2).format('DD/MM/YYYY')
  var fecha = new Date();
  var id = Date.parse(fecha);
  var table = `
  <table id="${nameNoSpaces}_table_${id}" class="ui basic table" style="border-collapse: collapse; margin-top: 30px;">
  <thead>
  <tr>
    <th colspan="7" style="width: 88%;">
      <button type="button" onclick="modal_fila('${nameNoSpaces}_tbody_${id}', '${nameNoSpaces}_modulo_${id}')"
        style="background-color: #FFC600; color: white; padding: 0.5em 0.5em;" class="ui icon button">
        <i class="edit icon" style="font-size: 12px;"></i>
      </button>
      MÓDULO ${numModule}  (${name.toUpperCase()})
    </th>
    <th colspan="2" style="width: 12%;">
      <div class="ui fluid left icon transparent input">
        <input data-totalmodulo="1" onclick="deleteValInput($(this))" onkeyup="convertTextToMoney($(this))" 
        onblur="calculoTotalModule($(this))" onload="totalModule($(this))" type="text" class="modulo_total" id="${nameNoSpaces}_total_${id}"
          style="padding-left: 17px !important;">
        <i class="dollar sign icon" style="font-size: 14px !important;"></i>
      </div>
    </th>
  </tr>
</thead>
<tbody id="${nameNoSpaces}_tbody_${id}">
<tr>
<td style="border-left: 3px  #FFC600 solid; width: 9%;"><i class="arrows alternate icon icon-tramitologia"></i></td>
<td style="width: 7%;">0</td>
<td style="width: 19%;">
  <div class="ui fluid transparent  input">
    <input  type="text" class=""  placeholder="texto prueba" >
  </div>
</td>
<td style="width: 9%;">
  <div class="ui inline fluid dropdown dropdown-estatus">
    <div class="text" style="color: #FFC600;">
      Baja
    </div>
    <i class="dropdown icon"></i>
    <div class="menu">
      <div class="item" style="color: #FE0919;">
        Urgente
      </div>
      <div class="item" style="color: #FF8C00;">
        Alta
      </div>
      <div class="item" style="color: #00CF61;">
        Media
      </div>
      <div class="item" style="color: #FFC600;">
        Baja
      </div>
    </div>
  </div>
</td>
<td style="width: 19%;">
  <div class="ui indicating fluid progress" data-percent="100"
    style="max-width: 90%; margin-left: 0em !important;">
    <div class="bar">
      <div class="progress"></div>
    </div>
  </div>
</td>
<td style="width: 15%;">
  <div class="ui fluid transparent input" style="cursor: pointer;">
    <input type="text" onload="LoadCalendar($(this))" onblur="BluerCalendar($(this))" class="date_range" name="datefilter"
    value="${today} - ${twoDays}"/>
  </div>
</td>
<td style="width: 10%;">
  <div class="ui fluid left icon transparent input porcentajeDiv">
    <input type="text" class="porcentajeInput" value="0" style="padding-left: 17px !important;">
    <i class="percent icon" style="font-size: 14px !important;" style="font-size: 14px !important;"></i>
  </div>
</td>
<td style="width: 8%;">
  <div class="ui fluid left icon transparent input numeros">
    <input type="text" onclick="deleteValInput($(this))" onkeyup="convertTextToMoney($(this))"
    onblur="calculoTotalModule($(this))"
    onload="LoadCosto($(this), '${nameNoSpaces}_total_${id}')" class="costos" value="0"
      style="padding-left: 25px !important;">
    <i class="dollar sign icon" style="font-size: 14px !important;"></i>
  </div>
</td>
<td style="width: 4%;">
  <i class="trash icon icon-tramitologia"></i>
</td>
</tr>
</tbody>
  </table>
  
  `
  $(table).appendTo('#container-desktop');
  $('.ui.inline.dropdown').dropdown();
LoadClass();
}
// html fila
htmlFilaTableModule = (bodyTable, TotalTable) => {
  
  var tablesTotales = $('#'+bodyTable+' > tr').toArray().length
  let today = moment().format('DD/MM/YYYY');
  let twoDays = moment().add('days', 2).format('DD/MM/YYYY')
  fila = `<tr>
  <td style="border-left: 3px  #FFC600 solid; width: 9%;"><i class="arrows alternate icon icon-tramitologia"></i></td>
  <td style="width: 7%;">${tablesTotales}</td>
  <td style="width: 19%;">
    <div class="ui fluid transparent  input">
      <input  type="text" class=""  placeholder="texto prueba" >
    </div>
  </td>
  <td style="width: 9%;">
    <div class="ui inline fluid dropdown dropdown-estatus">
      <div class="text" style="color: #FFC600;">
        Baja
      </div>
      <i class="dropdown icon"></i>
      <div class="menu">
        <div class="item" style="color: #FE0919;">
          Urgente
        </div>
        <div class="item" style="color: #FF8C00;">
          Alta
        </div>
        <div class="item" style="color: #00CF61;">
          Media
        </div>
        <div class="item" style="color: #FFC600;">
          Baja
        </div>
      </div>
    </div>
  </td>
  <td style="width: 19%;">
    <div class="ui indicating fluid progress" data-percent="100"
      style="max-width: 90%; margin-left: 0em !important;">
      <div class="bar">
        <div class="progress"></div>
      </div>
    </div>
  </td>
  <td style="width: 15%;">
    <div class="ui fluid transparent input" style="cursor: pointer;">
      <input type="text" onload="LoadCalendar($(this))" onblur="BluerCalendar($(this))" class="date_range" name="datefilter"
      value="${today} - ${twoDays}"/>
    </div>
  </td>
  <td style="width: 10%;">
    <div class="ui fluid left icon transparent input porcentajeDiv">
      <input type="text" 
      class="porcentajeInput" value="0" style="padding-left: 17px !important;">
      <i class="percent icon" style="font-size: 14px !important;" style="font-size: 14px !important;"></i>
    </div>
  </td>
  <td style="width: 8%;">
    <div class="ui fluid left icon transparent input numeros">
      <input type="text" onclick="deleteValInput($(this))" onkeyup="convertTextToMoney($(this))"
      onblur="calculoTotalModule($(this))"
      onload="LoadCosto($(this), '${TotalTable}')" class="costos" value="0"
        style="padding-left: 25px !important;">
      <i class="dollar sign icon" style="font-size: 14px !important;"></i>
    </div>
  </td>
  <td style="width: 4%;">
    <i class="trash icon icon-tramitologia"></i>
  </td>
</tr>`
$(fila).appendTo('#'+bodyTable);
$('.ui.inline.dropdown').dropdown();
LoadClass();
}