<template>
  <div class="periodic-table">
    <ElementSquare name="H"/>
    <BlankElementSquare v-for="index in 16"/>
    <ElementSquare name="He"/>

    <ElementSquare name="Li"/>
    <ElementSquare name="Be"/>
    <BlankElementSquare v-for="index in 10"/>
    <ElementSquare name="B"/>
    <ElementSquare name="C"/>
    <ElementSquare name="N"/>
    <ElementSquare name="O"/>
    <ElementSquare name="F"/>
    <ElementSquare name="Ne"/>

    <ElementSquare name="Na"/>
    <ElementSquare name="Ng"/>
    <BlankElementSquare v-for="index in 10"/>
    <ElementSquare name="Al"/>
    <ElementSquare name="Si"/>
    <ElementSquare name="P"/>
    <ElementSquare name="S"/>
    <ElementSquare name="Cl"/>
    <ElementSquare name="Ar"/>

    <ElementSquare name="K"/>
    <ElementSquare name="Ca"/>
    <ElementSquare name="Sc"/>
    <ElementSquare name="Ti"/>
    <ElementSquare name="V"/>
    <ElementSquare name="Cr"/>
    <ElementSquare name="Mn"/>
    <ElementSquare name="Fe"/>
    <ElementSquare name="Co"/>
    <ElementSquare name="Ni"/>
    <ElementSquare name="Cu"/>
    <ElementSquare name="Zn"/>
    <ElementSquare name="Ga"/>
    <ElementSquare name="Ge"/>
    <ElementSquare name="As"/>
    <ElementSquare name="Se"/>
    <ElementSquare name="Br"/>
    <ElementSquare name="Kr"/>

    <ElementSquare name="Rb"/>
    <ElementSquare name="Sr"/>
    <ElementSquare name="Y"/>
    <ElementSquare name="Zr"/>
    <ElementSquare name="Nb"/>
    <ElementSquare name="Mo"/>
    <ElementSquare name="Tc"/>
    <ElementSquare name="Ru"/>
    <ElementSquare name="Rh"/>
    <ElementSquare name="Pd"/>
    <ElementSquare name="Ag"/>
    <ElementSquare name="Cd"/>
    <ElementSquare name="In"/>
    <ElementSquare name="Sn"/>
    <ElementSquare name="Sb"/>
    <ElementSquare name="Te"/>
    <ElementSquare name="I"/>
    <ElementSquare name="Xe"/>

    <ElementSquare name="Cs"/>
    <ElementSquare name="Ba"/>
    <ElementSquare name="La"/>
    <ElementSquare name="Hf"/>
    <ElementSquare name="Ta"/>
    <ElementSquare name="W"/>
    <ElementSquare name="Re"/>
    <ElementSquare name="So"/>
    <ElementSquare name="Ir"/>
    <ElementSquare name="Pt"/>
    <ElementSquare name="Au"/>
    <ElementSquare name="Hg"/>
    <ElementSquare name="Tl"/>
    <ElementSquare name="Pb"/>
    <ElementSquare name="Bi"/>
    <ElementSquare name="Po"/>
    <ElementSquare name="At"/>
    <ElementSquare name="Rn"/>

    <ElementSquare name="Fr"/>
    <ElementSquare name="Ra"/>
    <ElementSquare name="Ac"/>
    <ElementSquare name="Rf"/>
    <ElementSquare name="Db"/>
    <ElementSquare name="Sg"/>
    <ElementSquare name="Bh"/>
    <ElementSquare name="Hs"/>
    <ElementSquare name="Mt"/>
    <ElementSquare name="Ds"/>
    <ElementSquare name="Rg"/>
    <ElementSquare name="Cn"/>
    <ElementSquare name="Nh"/>
    <ElementSquare name="Fl"/>
    <ElementSquare name="Mc"/>
    <ElementSquare name="Lv"/>
    <ElementSquare name="Ts"/>
    <ElementSquare name="Og"/>

    <BlankElementSquare v-for="index in 18"/>

    <BlankElementSquare v-for="index in 2"/>
    <ElementSquare name="Ce"/>
    <ElementSquare name="Pr"/>
    <ElementSquare name="Nd"/>
    <ElementSquare name="Pm"/>
    <ElementSquare name="Sm"/>
    <ElementSquare name="Eu"/>
    <ElementSquare name="Gd"/>
    <ElementSquare name="Tb"/>
    <ElementSquare name="Dy"/>
    <ElementSquare name="Ho"/>
    <ElementSquare name="Er"/>
    <ElementSquare name="Tm"/>
    <ElementSquare name="Yb"/>
    <ElementSquare name="Lu"/>
    <BlankElementSquare v-for="index in 2"/>

    <BlankElementSquare v-for="index in 2"/>
    <ElementSquare name="Th"/>
    <ElementSquare name="Pa"/>
    <ElementSquare name="U"/>
    <ElementSquare name="Np"/>
    <ElementSquare name="Pu"/>
    <ElementSquare name="Am"/>
    <ElementSquare name="Cm"/>
    <ElementSquare name="Bk"/>
    <ElementSquare name="Cf"/>
    <ElementSquare name="Es"/>
    <ElementSquare name="Fm"/>
    <ElementSquare name="Md"/>
    <ElementSquare name="No"/>
    <ElementSquare name="Lr"/>
    <BlankElementSquare v-for="index in 2"/>
  </div>
</template>

<script>
import ElementSquare from "./ElementSquare.vue"
import BlankElementSquare from "./BlankElementSquare.vue"

export default {
  name: "PeriodicTable"
}
</script>

<style scoped>
.periodic-table {
  display: flex;

  flex-flow: row wrap;
  justify-content: space-around;
}
</style>
