$(document).ready(function () {
    $('#search').keyup( (e)=>{
        search = $('#search').val()
        fetch('api/filter?inn='+search).then(res=>res.json()).then(result=>console.log(result))
    })

    $('#opener').on('click', ()=>{
        $('#slide').toggle(100)
        $('#short_search').toggle(100)
    })
    
});