<template>
    <div class="fetch-account">
        <h3>Import Character</h3>
        <button @click="clearAccount">X</button>
        <input v-if="characters.length == 0" v-model="account_name" type="text" placeholder="PoE Account">
        <input v-else v-model="account_name" type="text" disabled>
        <button v-if="characters.length == 0" @click="fetchCharacters">Go</button>
        <select v-if="characters.length >= 1" v-model="selected_char">
            <option disabled value="">Select Character</option>
            <option v-for="character in characters" :value="character">
                {{character.league}} {{ character.level }}, {{character.name}}, {{character.class}}
            </option>
        </select>
        <button v-if="selected_char != ''" @click="trackCharacter">Track</button>
        <p v-if="message">{{message}}</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            account_name: "",
            characters: [],
            selected_char: "",
            message: false,
        }
    },
    methods: {
        async fetchCharacters(e){
            this.message = false
            let response = await fetch("http://127.0.0.1:8000/api/get-characters", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({account_name: this.account_name})
            })
            let result = await response.json()
            if (result.startsWith('Status')){
                this.message = result
            }
            else {
                this.characters = JSON.parse(result)
            }
        },
        clearAccount(){
            this.account_name = ""
            this.characters = []
            this.selected_char = ""
            this.message = false
        },
        async trackCharacter(){
            let request = await fetch("http://127.0.0.1:8000/api/characters/" + this.account_name, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    account: {
                        account_name: this.account_name,
                    },
                    character: this.selected_char.name,
                    league: this.selected_char.league,
                    tracked: true
                })
            })
            if (request.ok) {
                this.message = "Character now tracked"
            }
        }
    }
}
</script>

<style scoped>
    .fetch-account {
        border-width: 1px;
        border-style: solid;
    }
</style>