<template>
    <div>
        <h1>Create Recipes Below!</h1>
    </div>

    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Recipe Name:</label>
                <input type="text" maxlength="100" required="" id="id_name">
            </p>

            <p>
                <label for="id_director">Food Description:</label>
                <input type="text" maxlength="500" required="" id="id_food_description">
            </p>

                <button type="submit" class="btn btn-primary">
                    Submit
                </button>                    
        </form>
    </div>

</template>

<script>
export default {
    name: 'App',
  components: {
  },
  props: [
  ],
  data: function() {
    return {
        csrf_token: ext_csrf_token,

        // csrf_token: ext_csrf_token,
	    // 	update_bis_url: ext_update_bis_url,
	    // 	form: ext_form,
	    // 	movie_dico: ext_movie_dict,
	    // 	actor_list_source: ext_actor_list,
	    // 	date: this.init_date(ext_movie_dict.release_date),
	    // 	time: this.init_time(ext_movie_dict.running_time),
	    // 	actor_list: ext_movie_dict.actors,
	    // 	submitting_form: false,
	    // 	form_error: [],
	    // 	form_updated: "",
    }
  },
  computed: {
  },
  methods: {

//      submit_form(){
//             if (this.submitting_form === true) {
//             return;
//             }
//             this.submitting_form = true
//             var form = document.createElement('form');
//             form.setAttribute('method', 'post');
//             let form_data = {
//                 'csrfmiddlewaretoken': this.csrf_token,
//                 'name': this.movie_dico.name,
//                 'running_time': this.get_time_string,
//                 'director': this.movie_dico.director,
//                 'release_date': this.get_date_string,
//             }
//             console.log('actor_list', this.actor_list)
//             console.log("form_data", form_data)
//             for (var key in form_data) {
//                 var html_field = document.createElement('input')
//                 html_field.setAttribute('type', 'hidden')
//                 html_field.setAttribute('name', key)
//                 html_field.setAttribute('value', form_data[key])
//                 form.appendChild(html_field)
//             }
//             var actor_field = document.createElement('select')
//             actor_field.setAttribute('name', 'actors')
//             actor_field.setAttribute('id', 'id_actors')
//             actor_field.setAttribute('multiple', '')
//             for (var actor of this.actor_list) {
//                 console.log('actor', actor)
//                 var option_field = document.createElement('option')
//                 option_field.setAttribute('value', actor.id)
//                 option_field.setAttribute('selected', '')
//                 actor_field.appendChild(option_field)
//             }
//             form.appendChild(actor_field)
//             document.body.appendChild(form);
//             form.submit()
//         },

//         submit_form_fetch(){
//         	this.form_error = []
//         	this.form_updated = ""
//         	let formData = new FormData();
//         	let form_data = {
// 	            	'name': this.movie_dico.name,
// 	            	'running_time': this.get_time_string,
// 	            	'director': this.movie_dico.director,
// 	            	'release_date': this.get_date_string,
//         	}
//         	for (var key in form_data) {
//             		formData.append(key, form_data[key])
//         	}
//         	this.actor_list.map(dic => formData.append('actors', dic.id))
//         	fetch(this.update_bis_url,
//             	{
//                 	method: "post",
//                 	body: formData,
//                 	headers: {'X-CSRFToken': this.csrf_token},
//                 	credentials: 'same-origin'
//             	}
//         	).then(function(response) {
//             	console.log('response', response)
//             	return response.json()}).then(
// 	            	this.handleResponse).catch(
// 	                	(error) => {
// 	                	console.log('error', String(error))
// 	                	this.form_error=["error"]
//     			})
//     	},
//     	handleResponse(response) {
//         	console.log('json response', response)
//         	if ('success' in response){
// 	            	if (response['success'] == true) {
// 	                	this.form_updated = "Movie has been updated"
// 	            	} else {
// 	                	if ('errors' in response){
// 		                    	for (const [key, value] of Object.entries(response['errors'])) {
// 		                        	for (const error of value) {
// 		                            		this.form_error.push(`${key}: ${error}`)
// 		                        	}
// 	                    		}
// 	                	} else {
// 	                    		this.form_error=["Update failed - An error occurred but do not have more information about it"]
// 	                	}
// 	            	}
// 		} else {
// 	            	this.form_error=["Update failed - It has been an error on the form request"]
// 		}
//     	}
//     },
//   },
  },
  watch: {
  }
}
</script>


