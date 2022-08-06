<template>
    <div class="snapshot-detail">
        <apexchart @mounted="selectFirst" @dataPointSelection="selectSnapshot" ref="chart" height="600" type="bar" :options="chart_options" :series="chart_data"></apexchart>
        <div class="controls">
            <button @click="prevSnapshot">Previous</button>
            <span>{{snapshots[current_snapshot_number].time}}</span>
            <button @click="nextSnapshot">Next</button>
        </div>
        <character-inventory v-if="snapshots.length >= 1" :items="snapshots[current_snapshot_number].items" v-model="selected_item"/>
        <jewels v-if="snapshots.length >= 1" :items="snapshots[current_snapshot_number].passives.items"/>
        <item-info v-if="selected_item" :item="selected_item"/>
    </div>
</template>
<script>
import VueApexCharts from "vue3-apexcharts"
import CharacterInventory from "@/components/CharacterInventory.vue"
import Jewels from "./Jewels.vue"
import ItemInfo from "@/components/ItemInfo.vue"
import * as MyUtils from "@/modules/myutils.js"

export default {
    components: {
        apexchart: VueApexCharts,
        CharacterInventory,
        Jewels,
        ItemInfo
    },
    props: ['snapshots', 'chart_data', 'chart_options'],
    data() {
        return {
            current_snapshot_number: 0,
            selected_item: {}
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
    .controls {
        text-align: center;
        grid-column-start: 1;
        grid-column-end: 3;
    }
    .snapshot-detail {
        display: grid;
        grid-template-columns: 1fr 1fr;
        padding: 0 2rem;
    }
    .vue-apexcharts {
        grid-column-start: 1;
        grid-column-end: 3;
    }
</style>