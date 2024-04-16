

const loggingStore = {
    state: () => ({
        logSocket: null,
        uuid: '', 
        logging_consent_given: false,       
        exp: 'Compression Refrigeration',                     
        hardware: '',                
        course: '',                      //GETS SET IN STREAMS.VUE FROM URL QUERY PARAM
        saved: [],

       }),
       mutations:{
            SET_LOG_SOCKET(state, socket){
                state.logSocket = socket;
            },
            SET_LOGGING_CONSENT(state, consent){
                state.logging_consent_given = consent;
            },
            SET_UUID(state, uuid){
                state.uuid = uuid;
            },
            SET_EXPERIMENT(state, exp){
                state.exp = exp;
            },
            SET_HARDWARE(state, hardware){
                state.hardware = hardware;
            },
            SET_COURSE(state, course){
                state.course = course;
            },
            SET_SAVED(state, data){
                state.saved = data;
            },
            // THIS is just for testing to allow mock logging to the analytics client.
            MOCK_LOG_ANALYTICS(state, payload){
                if(state.logging_consent_given && state.logSocket != null){
                    state.logSocket.send(JSON.stringify({
                        user: state.uuid,
                        t: Date.now(),          
                        exp: state.exp,
                        hardware: state.hardware,
                        course: state.course,
                        type: "analytics",       
                        payload: payload
                    }));
                }
            },  
            // For logging to the background logging server, not to analytics
            LOG(state, payload){
                if(state.logging_consent_given && state.logSocket != null){
                    state.logSocket.send(JSON.stringify({
                        user: state.uuid,
                        t: Date.now(),          
                        exp: state.exp,
                        //hardware: state.hardware,     //analytics is not aligned with any single piece of hardware
                        course: state.course,
                        type: "log",       
                        payload: payload
                    }));
                }
            },
            REQUEST(state, payload){
                if(state.logging_consent_given && state.logSocket != null){
                    state.logSocket.send(JSON.stringify({
                        user: state.uuid,
                        t: Date.now(),          
                        exp: state.exp,   
                        course: state.course, 
                        type: "request", 
                        payload: payload   
                    }));
                }
            }, 
            FEEDBACK(state, payload){
                if(state.logging_consent_given && state.logSocket != null){
                    state.logSocket.send(JSON.stringify({
                        user: state.uuid,
                        t: Date.now(),          
                        exp: state.exp, 
                        course: state.course,
                        type: "feedback",       
                        payload: payload
                    }));
                }
                
                
            },

       },
       actions:{
            setLogSocket(context, socket){
                context.commit('SET_LOG_SOCKET', socket);
            },
            setLoggingConsent(context, consent){
                context.commit('SET_LOGGING_CONSENT', consent);
            },
            setUUID(context, uuid){
                context.commit('SET_UUID', uuid);
            },
            setExperiment(context, exp){
                context.commit('SET_EXPERIMENT', exp);
            },
            setHardware(context, hardware){
                context.commit('SET_HARDWARE', hardware);
            },
            setCourse(context, course){
                context.commit('SET_COURSE', course);
            },
            setSaved(context, data){
                context.commit('SET_SAVED', data);
            },
            //for testing only
            mockLogAnalytics(context, payload){
                context.commit('MOCK_LOG_ANALYTICS', payload);
            },
            log(context, payload){
                context.commit('LOG', payload);
            },
            async request(context, payload){
                context.commit('REQUEST', payload);
                await helpers.delay(100);
                context.commit('LOG', {log:"analytics-interaction", type: "request"});
            },
            requestAll(context){
                if(context.state.exp == 'spinner'){
                    if(context.state.course == 'cie3'){
                        context.commit('REQUEST', {"content": 'all_feedback', "graph": 'spinner-cie3-1-2'}); 
                    } else{
                        context.commit('REQUEST', {"content": 'all_feedback', "graph": 'spinner-engdes1-1-core'}); 
                    }
                } else if(context.state.exp == 'pendulum'){
                    if(context.state.course == 'engdes1'){
                        context.commit('REQUEST', {"content": 'all_feedback', "graph": 'pendulum-engdes1-1-core'}); 
                    } else{
                        context.commit('REQUEST', {"content": 'all_feedback', "graph": 'pendulum-engdes1-1-core'}); 
                    }
                }
            },
            async feedback(context, payload){
                context.commit('FEEDBACK', payload);
                await helpers.delay(100);
                context.commit('LOG', {log:"analytics-interaction", type: "feedback"});
            }

       },
       getters:{
           getLogSocket(state){
                return state.logSocket;
           },
           getLogConsent(state){
            return state.logging_consent_given;
            },
            getLogUUID(state){
                return state.uuid;
            },
            getExperiment(state){
                return state.exp
            },
            getHardware(state){
                return state.hardware
            },
            getCourse(state){
                return state.course
            },
            getSaved(state){
                return state.saved;
            }
          
       },  
  
  }

  let helpers = {
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    },
  }

  export default loggingStore;
