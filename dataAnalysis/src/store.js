import { createStore } from 'vuex'
import uiStore from './modules/uiStore.js'
import streamStore from './modules/streamStore.js'
import logging from './modules/logging.js'


const store = createStore({
    modules:{
        ui: uiStore,
        stream: streamStore,
        logging: logging,
    }
})

export default store;