<template>
    <div>
        <apexchart @mounted="selectFirst" @dataPointSelection="selectSnapshot" ref="chart" width="500" type="bar" :options="chart_options" :series="chart_data"></apexchart>
        <div>
            <button @click="prevSnapshot">Previous</button>
            <span>{{snapshots[current_snapshot_number].time}}</span>
            <button @click="nextSnapshot">Next</button>
        </div>
        <character-inventory v-if="snapshots.length >= 1" :items="snapshots[current_snapshot_number].items"/>
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
    props: ['snapshots', 'chart_data', 'chart_options'],
    data() {
        return {
            current_snapshot_number: 0
        }
    },
    methods: {
        selectFirst(){
            this.$refs.chart.toggleDataPointSelection(0, 0)
        },
        selectSnapshot(event, chartContext, config){
            this.current_snapshot_number = config.selectedDataPoints
        },
        nextSnapshot(){
            if (this.current_snapshot_number == this.snapshots.length - 1){
                this.current_snapshot_number = 0
            }
            else {
                this.current_snapshot_number++
            }
            this.$refs.chart.toggleDataPointSelection(0, this.current_snapshot_number)
        },
        prevSnapshot(){
            if (this.current_snapshot_number == 0){
                this.current_snapshot_number = this.snapshots.length - 1
            }
            else {
                this.current_snapshot_number--
            }
            this.$refs.chart.toggleDataPointSelection(0, this.current_snapshot_number)
        },
    },
}
</script>
<style>
    
</style>