<template>
  <CContainer>
    <h2>Banned Countries</h2>

    <div>
      <p>Banned</p>
      <div class="d-flex">
        <CButton
            v-for="country in selectedCountries"
            :key="country.code"
            class="mr-2"
            color="info">
          {{ country.name }}
        </CButton>
      </div>
    </div>

    <div class="mt-5">
      <p>Select Banned Countries</p>
      <CTabs variant="pills" :active-tab="0">
        <CTab title="ABC">
          <CInputCheckbox
              v-for="country in countryList"
              :key="country.code"
              :label="country.name"
              @update:checked="addCountry(country, $event)"/>
          <CInputCheckbox label="Philippines" @update:checked="addCountry('Philippines', $event)"/>
        </CTab>
      </CTabs>
    </div>
  </CContainer>
</template>

<script>
// todo: move to backend
import countriesJson from './countries.json';

export default {
  name: 'ApplicantTest',
  mounted() {
    console.log(countriesjson);
  },
  data() {
    return {
      selectedCountries: [],
      countryList: countriesJson
    }
  },
  methods: {
    addCountry(country, checked) {
      if (checked)
        this.selectedCountries.push(country);
      else
        this.selectedCountries = this.selectedCountries.filter((c) => c !== country)
    }
  }
}
</script>
