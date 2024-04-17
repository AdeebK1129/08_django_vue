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
                <label for="id_ingredients">Ingredients:</label><br>
				<multiselect type="hidden" v-model="ingredient_list" name="ingredients" required="" id="id_ingredients" :options="ingredient_list_source" multiple="" label="name" track-by="name" >
				</multiselect>
            </p>

            <p>
                <label for="id_food_description">Food Description:</label>
                <input type="text" maxlength="500" required="" id="id_food_description">
            </p>

            <p>
                <label for="id_recipe">Recipe:</label>
                <input type="text" maxlength="500" required="" id="id_recipe">
            </p>

                <button type="submit" class="btn btn-primary">
                    Submit
                </button>                    
        </form>
    </div>

</template>

<script>
import Multiselect from 'vue-multiselect'

export default {
    name: 'App',
  components: {
    Multiselect
  },
  props: [
  ],
  data: function() {
    return {
        csrf_token: ext_csrf_token,
        form: ext_form,
        recipe_dico: ext_recipe_dict,
        ingredient_list_source: ext_ingredient_list,
        ingredient_list: ext_recipe_dict.ingredients,
        submitting_form: false,
        form_error: [],
        form_updated: "",

    }
  },
  computed: {
  },
  methods: {
    submit_form(){
            if (this.submitting_form === true) {
                return;
            }
            this.submitting_form = true
            var form = document.createElement('form');
            form.setAttribute('method', 'post');
            let form_data = {
                'csrfmiddlewaretoken': this.csrf_token,
                'name': this.recipe_dico.name,
                'foodDescription': this.recipe_dico.foodDescription,
                'recipe': this.recipe_dico.recipe,
            }
            console.log('ingredient_list', this.ingredient_list)
            console.log("form_data", form_data)
            for (var key in form_data) {
                var html_field = document.createElement('input')
                html_field.setAttribute('type', 'hidden')
                html_field.setAttribute('name', key)
                html_field.setAttribute('value', form_data[key])
                form.appendChild(html_field)
            }
            var ingredient_field = document.createElement('select')
            ingredient_field.setAttribute('name', 'ingredients')
            ingredient_field.setAttribute('id', 'id_ingredients')
            ingredient_field.setAttribute('multiple', '')
            for (var ingredient of this.ingredient_list) {
                console.log('ingredient', ingredient)
                var option_field = document.createElement('option')
                option_field.setAttribute('value', ingredient.id)
                option_field.setAttribute('selected', '')
                ingredient_field.appendChild(option_field)
            }
            form.appendChild(ingredient_field)
            document.body.appendChild(form);
            form.submit()
        },
  },
  watch: {
  }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>

