<template>
    <div>
        <h1>Create Recipes Below!</h1>
    </div>

    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Recipe Title: </label> &nbsp;
                <input type="text" name="name" v-model="title" maxlength="100"
                required="" id="id_name">
            </p>
            
            <p>
                <label for="id_ingredients">Ingredients:</label>
                <select hidden name="ingredients"  id="id_ingredients" multiple="">
                    <option v-for="ingredient in ingredient_list" :value="ingredient.id" selected=""></option>
                </select>
                <multiselect v-model="ingredient_list" :options="ingredient_list_source" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Choose the ingredients" label="name" track-by="name" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
                    <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
                </multiselect>
            </p>

            <p>
                <label for="id_foodDescription">Description: </label>&nbsp;
                <input type="hidden" :value="foodDescription" name="foodDescription" value=""
                maxlength="5000" required="" id="id_foodDescription"  >
                <textarea v-model="foodDescription" name="foodDescription" cols="50" maxlength="5000" rows="3"> </textarea>
            </p>

            <p>
                <label for="id_recipe">Recipe: </label>&nbsp;
                <input type="hidden" :value="recipe" name="recipe" value=""
                maxlength="5000" required="" id="id_recipe"  >
                <textarea v-model="recipe" name="recipe" cols="50" maxlength="5000" rows="3"> </textarea>
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
        title: ext_recipe_dict.name,
        foodDescription: ext_recipe_dict.foodDescription,
        recipe: ext_recipe_dict.recipe,
        ingredient_list_source: (ext_ingredient_list != undefined) ? ext_ingredient_list: [],
        submitting_form: false,
        form_error: [],
        form_updated: "",
        foodDescription: ext_recipe_dict.foodDescription,
        update_bis_url: ext_update_bis_url,
        ingredient_list: (ext_recipe_dict.ingredients != undefined && ext_recipe_dict.ingredients != null) ? ext_recipe_dict.ingredients : [],
    }
  },
  computed: {
    onLoad() {
        console.log("hello");
        console.log(this.ingredient_list_source);
        console.log(this.ingredient_list);
        console.log(this.recipe_dico);
        console.log(this.csrf_token)
    }
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
  mounted(){
            this.csrf_token=ext_csrf_token;
            this.recipe_dico=ext_recipe_dict;  
            this.ingredient_list_source= ext_ingredient_list;
            this.ingredient_list = JSON.parse(ext_recipe_dict.ingredients);
    },
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>

