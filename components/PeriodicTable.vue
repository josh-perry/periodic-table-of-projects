<template>
  <div class="periodic-table">
    <ElementSquare :element="Elements['Hydrogen']"/>
    <BlankElementSquare v-for="index in 16"/>
    <ElementSquare :element="Elements['Helium']"/>

    <ElementSquare :element="Elements['Lithium']"/>
    <ElementSquare :element="Elements['Beryllium']"/>
    <BlankElementSquare v-for="index in 10"/>
    <ElementSquare :element="Elements['Boron']"/>
    <ElementSquare :element="Elements['Carbon']"/>
    <ElementSquare :element="Elements['Nitrogen']"/>
    <ElementSquare :element="Elements['Oxygen']"/>
    <ElementSquare :element="Elements['Fluorine']"/>
    <ElementSquare :element="Elements['Neon']"/>

    <ElementSquare :element="Elements['Sodium']"/>
    <ElementSquare :element="Elements['Magnesium']"/>
    <BlankElementSquare v-for="index in 10"/>
    <ElementSquare :element="Elements['Aluminum']"/>
    <ElementSquare :element="Elements['Silicon']"/>
    <ElementSquare :element="Elements['Phosphorus']"/>
    <ElementSquare :element="Elements['Sulfur']"/>
    <ElementSquare :element="Elements['Chlorine']"/>
    <ElementSquare :element="Elements['Argon']"/>

    <ElementSquare :element="Elements['Potassium']"/>
    <ElementSquare :element="Elements['Calcium']"/>
    <ElementSquare :element="Elements['Scandium']"/>
    <ElementSquare :element="Elements['Titanium']"/>
    <ElementSquare :element="Elements['Vanadium']"/>
    <ElementSquare :element="Elements['Chromium']"/>
    <ElementSquare :element="Elements['Manganese']"/>
    <ElementSquare :element="Elements['Iron']"/>
    <ElementSquare :element="Elements['Cobalt']"/>
    <ElementSquare :element="Elements['Nickel']"/>
    <ElementSquare :element="Elements['Copper']"/>
    <ElementSquare :element="Elements['Zinc']"/>
    <ElementSquare :element="Elements['Gallium']"/>
    <ElementSquare :element="Elements['Germanium']"/>
    <ElementSquare :element="Elements['Arsenic']"/>
    <ElementSquare :element="Elements['Selenium']"/>
    <ElementSquare :element="Elements['Bromine']"/>
    <ElementSquare :element="Elements['Krypton']"/>

    <ElementSquare :element="Elements['Rubidium']"/>
    <ElementSquare :element="Elements['Strontium']"/>
    <ElementSquare :element="Elements['Yttrium']"/>
    <ElementSquare :element="Elements['Zirconium']"/>
    <ElementSquare :element="Elements['Niobium']"/>
    <ElementSquare :element="Elements['Molybdenum']"/>
    <ElementSquare :element="Elements['Technetium']"/>
    <ElementSquare :element="Elements['Ruthenium']"/>
    <ElementSquare :element="Elements['Rhodium']"/>
    <ElementSquare :element="Elements['Palladium']"/>
    <ElementSquare :element="Elements['Silver']"/>
    <ElementSquare :element="Elements['Cadmium']"/>
    <ElementSquare :element="Elements['Indium']"/>
    <ElementSquare :element="Elements['Tin']"/>
    <ElementSquare :element="Elements['Antimony']"/>
    <ElementSquare :element="Elements['Tellurium']"/>
    <ElementSquare :element="Elements['Iodine']"/>
    <ElementSquare :element="Elements['Xenon']"/>

    <ElementSquare :element="Elements['Cesium']"/>
    <ElementSquare :element="Elements['Barium']"/>
    <ElementSquare :element="Elements['Lanthanum']"/>
    <ElementSquare :element="Elements['Hafnium']"/>
    <ElementSquare :element="Elements['Tantalum']"/>
    <ElementSquare :element="Elements['Tungsten']"/>
    <ElementSquare :element="Elements['Rhenium']"/>
    <ElementSquare :element="Elements['Osmium']"/>
    <ElementSquare :element="Elements['Iridium']"/>
    <ElementSquare :element="Elements['Platinum']"/>
    <ElementSquare :element="Elements['Gold']"/>
    <ElementSquare :element="Elements['Mercury']"/>
    <ElementSquare :element="Elements['Thallium']"/>
    <ElementSquare :element="Elements['Lead']"/>
    <ElementSquare :element="Elements['Bismuth']"/>
    <ElementSquare :element="Elements['Polonium']"/>
    <ElementSquare :element="Elements['Astatine']"/>
    <ElementSquare :element="Elements['Radon']"/>

    <ElementSquare :element="Elements['Francium']"/>
    <ElementSquare :element="Elements['Radium']"/>
    <ElementSquare :element="Elements['Actinium']"/>

    <ElementSquare :element="Elements['Rutherfordium']"/>
    <ElementSquare :element="Elements['Dubnium']"/>
    <ElementSquare :element="Elements['Seaborgium']"/>
    <ElementSquare :element="Elements['Bohrium']"/>
    <ElementSquare :element="Elements['Hassium']"/>
    <ElementSquare :element="Elements['Meitnerium']"/>
    <ElementSquare :element="Elements['Darmstadtium']"/>
    <ElementSquare :element="Elements['Roentgenium']"/>
    <ElementSquare :element="Elements['Copernicium']"/>
    <ElementSquare :element="Elements['Nihonium']"/>
    <ElementSquare :element="Elements['Flerovium']"/>
    <ElementSquare :element="Elements['Moscovium']"/>
    <ElementSquare :element="Elements['Livermorium']"/>
    <ElementSquare :element="Elements['Tennessine']"/>
    <ElementSquare :element="Elements['Oganesson']"/>

    <BlankElementSquare v-for="index in 18"/>
    <BlankElementSquare v-for="index in 2"/>
    <ElementSquare :element="Elements['Cerium']"/>
    <ElementSquare :element="Elements['Praseodymium']"/>
    <ElementSquare :element="Elements['Neodymium']"/>
    <ElementSquare :element="Elements['Promethium']"/>
    <ElementSquare :element="Elements['Samarium']"/>
    <ElementSquare :element="Elements['Europium']"/>
    <ElementSquare :element="Elements['Gadolinium']"/>
    <ElementSquare :element="Elements['Terbium']"/>
    <ElementSquare :element="Elements['Dysprosium']"/>
    <ElementSquare :element="Elements['Holmium']"/>
    <ElementSquare :element="Elements['Erbium']"/>
    <ElementSquare :element="Elements['Thulium']"/>
    <ElementSquare :element="Elements['Ytterbium']"/>
    <ElementSquare :element="Elements['Lutetium']"/>
    <BlankElementSquare v-for="index in 2"/>

    <BlankElementSquare v-for="index in 2"/>
    <ElementSquare :element="Elements['Thorium']"/>
    <ElementSquare :element="Elements['Protactinium']"/>
    <ElementSquare :element="Elements['Uranium']"/>
    <ElementSquare :element="Elements['Neptunium']"/>
    <ElementSquare :element="Elements['Plutonium']"/>
    <ElementSquare :element="Elements['Americium']"/>
    <ElementSquare :element="Elements['Curium']"/>
    <ElementSquare :element="Elements['Berkelium']"/>
    <ElementSquare :element="Elements['Californium']"/>
    <ElementSquare :element="Elements['Einsteinium']"/>
    <ElementSquare :element="Elements['Fermium']"/>
    <ElementSquare :element="Elements['Mendelevium']"/>
    <ElementSquare :element="Elements['Nobelium']"/>
    <ElementSquare :element="Elements['Lawrencium']"/>
    <BlankElementSquare v-for="index in 2"/>
  </div>
</template>

<script>
import ElementSquare from "./ElementSquare.vue"
import BlankElementSquare from "./BlankElementSquare.vue"
import Elements from "../static/json/meta.json"

export default {
  name: "PeriodicTable",
  data({ $http }) {
    return {
      Elements
    };
  }
}
</script>

<style scoped>
.periodic-table {
  display: flex;

  flex-flow: row wrap;
  justify-content: space-around;
}
</style>
