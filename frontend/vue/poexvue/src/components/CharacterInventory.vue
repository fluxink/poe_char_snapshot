<template>
    <div class="mainInventoryPanel">
        <item-container v-for="item in items" :item="item"></item-container>
    </div>
</template>
<script>
import ItemContainer from '@/components/ItemContainer.vue'

export default {
    components: {ItemContainer},
    props: ['items'],
    data(){
        return{

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
    }
    .Boots {
        top: 312.6px;
        left: 368.9px;
    }
    .Helm {
        top: 100px;
        left: 252px;
    }
    .Ring2 {
        top: 253.6px;
        left: 182.69px;
    }
    .Ring {
        top: 253.6px;
        left: 369.9px
    }
    .Amulet {
        top: 194.58px;
        left: 369.9px
    }
    .Belt {
        top: 360px;
        left: 252px;
    }
    .Gloves {
        top: 312.6px;
        left: 135.22px;
    }
    .Offhand {
        top: 111.21px;
        left: 438.27px;
        height: 189.858px !important;
        min-width: 94.929px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .BodyArmour {
        top: 206.14px;
        left: 252px;
    }
    .Weapon {
        top: 111.21px;
        left: 65.85px;
        height: 189.858px !important;
        min-width: 94.929px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .Flask {
        display: none;
    }
    .Offhand2 {
        display: none;
    }
    .Weapon2 {
        display: none;
    }

</style>