<template>
    <div class="mainInventoryPanel">
        <item-container v-for="(item, index) in items" :item="item" @mouseenter="selectItem" :value="index"></item-container>
    </div>
</template>
<script>
import ItemContainer from '@/components/ItemContainer.vue'

export default {
    components: {ItemContainer},
    props: ['items'],
    data(){
        return{
            selected_item: {}
        }
    },
    methods: {
        selectItem(e){
            this.selected_item = this.items[e.target.attributes.value.value]
        }
    },
    watch: {
        selected_item(newValue){
            this.$emit("update:modelValue", newValue)
        }
    }
}
</script>
<style>
    .mainInventoryPanel {
        display: flex;
        border-width: 2px;
        border-style: solid;
        width: 600px;
        height: 524px;
        flex-wrap: wrap;
        align-items:flex-start;
        align-content:flex-start;
        position: relative;
        background: url("@/assets/MainInventoryNoBags.png");
        grid-column-start: 2;
    }
    .Boots {
        top: 312.6px;
        left: 368.9px;
    }
    /* .BootsInfo {
        bottom: 212px;
        left: calc(368.9px - 25% / 2);
    } */
    .Helm {
        top: 100px;
        left: 252px;
    }
    /* .HelmInfo {
        bottom: 424px;
        left: calc(252px - 50% / 2);
    } */
    .Ring2 {
        top: 253.6px;
        left: 369.9px;
    }
    /* .Ring2Info {
        bottom: 269.6px;
        left: calc(369.9px - 25% / 2);
    } */
    .Ring {
        top: 253.6px;
        left: 182.69px;
    }
    /* .RingInfo {
        bottom: 269.6px;
        left: calc(182.69px - 25% / 2);
    } */
    .Amulet {
        top: 194.58px;
        left: 369.9px;
    }
    /* .AmuletInfo {
        bottom: 329.58px;
        left: calc(369.9px - 25% / 2);
    } */
    .Belt {
        top: 360px;
        left: 252px;
    }
    /* .BeltInfo {
        bottom: 164px;
        left: calc(252px - 50% / 2);
    } */
    .Gloves {
        top: 312.6px;
        left: 135.22px;
    }
    /* .GlovesInfo {
        bottom: 212px;
        left: calc(135.22px - 25% / 2);
    } */
    .Offhand {
        top: 111.21px;
        left: 438.27px;
        height: 189.858px !important;
        min-width: 94.929px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    /* .OffhandInfo {
        bottom: 413.21px;
        left: calc(438.27px - 25% / 2);
    } */
    .BodyArmour {
        top: 206.14px;
        left: 252px;
    }
    /* .BodyArmourInfo {
        bottom: 318.14px;
        left: calc(252px - 25% / 2);
    } */
    .Weapon {
        top: 111.21px;
        left: 65.85px;
        height: 189.858px !important;
        min-width: 94.929px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    /* .WeaponInfo {
        bottom: 413.21px;
        left: calc(65.85px - 25% / 2);
    } */
    .Flask {
        top: 418.51px;
    }
    .Flask.x0 {
        left: 186.34px;
    }
    .Flask.x1 {
        left: 233.8px;
    }
    .Flask.x2 {
        left: 281.269px;
    }
    .Flask.x3 {
        left: 328.734px;
    }
    .Flask.x4 {
        left: 376.2px;
    }
    .Offhand2 {
        display: none;
    }
    .Weapon2 {
        display: none;
    }

</style>