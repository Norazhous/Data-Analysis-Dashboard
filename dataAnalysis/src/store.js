import { createStore } from 'vuex'
// import uiStore from './modules/uiStore.js'
// import logging from './modules/logging.js'
import dataStore from './modules/dataStore'


const store = createStore({
    modules:{
        // ui: uiStore,
        // logging: logging,
        data: dataStore,
    }
})

export default store;