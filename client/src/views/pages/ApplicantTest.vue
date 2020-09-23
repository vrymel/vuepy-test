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
          <span @click="removeCountry(country)">
            <CIcon name="cilXCircle" class="ml-3"/>
          </span>
        </CButton>
      </div>
    </div>

    <div class="mt-5">
      <p>Select Banned Countries</p>
      <CTabs variant="pills" :active-tab="0" @update:activeTab="selectCountryGroup">
        <CTab v-for="groupedCountry in countriesByFirstLetters"
              :key="groupedCountry.name"
              :title="groupedCountry.name">
        </CTab>
      </CTabs>

      <div>
        <CInputCheckbox
            v-for="country in displayCountryList"
            :key="country.code"
            :label="country.name"
            :checked="selectedCountriesMap[country.code]"
            @update:checked="addCountry(country, $event)">
          {{country}}
        </CInputCheckbox>
      </div>
    </div>
  </CContainer>
</template>

<script>
import chunk from 'lodash/chunk';
// todo: move to backend
import countriesJson from './countries.json';

export default {
  name: 'ApplicantTest',
  data() {
    return {
      selectedCountries: [],
      selectedCountriesMap: {},
      countryList: countriesJson,
      selectedCountryGroup: { name: 'ABC', data: ['A', 'B', 'C'] }
    }
  },
  computed: {
    countriesByFirstLetters: function () {
      const uniqueFirstHalf = new Set();
      for (let c of this.countryList) {
        let first = c.name[0];

        // Manually add MN later
        if (first !== 'M' && first !== 'N')
          uniqueFirstHalf.add(first);

        // No X in countryList so manually add it here
        if (uniqueFirstHalf.has('W'))
          uniqueFirstHalf.add('X');
      }

      const chunked = chunk(Array.from(uniqueFirstHalf), 3);
      chunked.splice(4, 0, ['M', 'N']);

      return chunked.map((chunk) => {
        return {
          'name': chunk.join(''),
          'data': chunk
        }
      })
    },
    displayCountryList: function() {
      const allowedFirstLetters = new Set(this.selectedCountryGroup.data);
      const displayCountries = [];

      for (let c of this.countryList) {
        if (allowedFirstLetters.has(c.name[0])) {
          displayCountries.push(c);
        }
      }

      return displayCountries;
    }
  },
  methods: {
    addCountry(country, checked) {
      if (checked) {
        this.selectedCountries.push(country);
        this.selectedCountriesMap[country.code] = true;
      } else {
        this.selectedCountries = this.selectedCountries.filter((c) => c !== country)
        delete this.selectedCountriesMap[country.code];
      }
    },
    removeCountry(country) {
      this.selectedCountries = this.selectedCountries.filter((c) => c !== country)
      delete this.selectedCountriesMap[country.code];
    },
    selectCountryGroup(selectedTabIndex) {
      this.selectedCountryGroup = this.countriesByFirstLetters[selectedTabIndex];
    }
  }
}
</script>
