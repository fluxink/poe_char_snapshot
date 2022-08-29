<template>
    <div class="get-snapshots">
        <h3>Get Snapshots</h3>
        <button @click="clearAccount">X</button>
        <input v-if="characters.length == 0" v-model="account" type="text" placeholder="PoE Account">
        <input v-else v-model="account" type="text" disabled>
        <button v-if="characters.length == 0" @click="fetchSavedCharacters">Get saved characters</button>
        <select v-if="characters.length >= 1" v-model="selected_character">
            <option disabled value="">Select Character</option>
            <option v-for="character in characters" :value="character.character">
                {{character.character}}
            </option>
        </select>
        <button v-if="characters.length >= 1" @click="fetchCharacterSnapshots">Retrive</button>
        <p v-if="message">{{message}}</p>
    </div>
</template>
<script>
import VueApexCharts from "vue3-apexcharts"
import CharacterInventory from "@/components/CharacterInventory.vue"
import * as MyUtils from "@/modules/myutils.js"

export default {
    components: {
        apexchart: VueApexCharts,
        CharacterInventory
    },
    data(){
        return {
            account: "",
            characters: [],
            snapshots: [],
            selected_character: "",
            chart_data: [],
            chart_options: [],
            message: false,
        }
    },
    methods: {
        async fetchSavedCharacters(){
            this.message = "Loading..."
            let response = await fetch("http://127.0.0.1:8000/api/accounts/" + this.account, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            if (response.ok) {
                let result = await response.json()
                this.characters = result
                this.message = false
            }
            else {
                this.message = response.statusText
            }
        },
        clearAccount(){
            this.account = ""
            this.characters = []
            this.snapshots = []
            this.current_snapshot_number = 0
        },
        async fetchCharacterSnapshots(){
            this.message = "Loading..."
            let response = await fetch("http://127.0.0.1:8000/api/snapshots/" + this.selected_character, {
                method: "GET"
            })
            if (response.ok) {
                let result = await response.json()
                this.message = false
                let data = MyUtils.getTimeAndExp(result)
                this.chart_options = {
                    xaxis: {
                        type: 'category',
                        categories: data[0],
                    },
                    yaxis: {
                        labels: {
                            formatter: MyUtils.numberWithCommas
                            }
                        },
                    chart: {
                        toolbar: {
                            show: false
                        },
                    },
                    title: {
                        text: 'Snapshots',
                        align: 'center'
                    }
                }

                this.chart_data = [{
                    name: 'Expirience',
                    data: data[1]
                }]
                this.snapshots = result
            }
            else {
                this.message = response.statusText
            }
        },
    },
    watch: {
        snapshots(newValue){
            this.$emit("update:modelValue", newValue)
        }
    }
}
</script>
<style scoped>
    .get-snapshots {
        border-width: 1px;
        border-style: solid;
    }
</style>