/**
 * 
 */

$(function){
	$('#search').keyup(functin()){
		
		$.ajax({
			type: "POST"
			url: "/article/search",
			data: {
				'search_text' : $('#search').val(),
				'casrfmiddlewaretoken' : $("input[name=scrfmiddlewaretoken]").val()				
			}
			success: searchSuccess
			dataType:'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR)
{
	$('#search-result'.html(data);)
	
}