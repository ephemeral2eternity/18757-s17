var fs = require('fs');
var util = require('util')

dir = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/data/planetlab-trace-superbowl-2017-0205Feb/';
count = 0;
fs.readdirSync( dir, function( err, files ) {
        if( err ) {
            console.error( "Could not list the directory.", err );
            process.exit( 1 );
        }
        files.forEach(function(file, index){
            flag = 1;
            path_file = dir + file;
            console.log(file);

            //checking if the trace route file is already there
            mm = '/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/traceRouteStep1Extraction/'
            fs.readdirSync(mm, function(err, files1){
                files1.forEach(function(file1,index){
                console.log(file1);
                    if(("trace-route-analysis_" + file) == file1){
                        console.log("Matches!");
                        flag = 0;
                    }
                });
            })

            if(flag!=0){
                console.log("Being Processed!");
                parsed_json_cache = JSON.parse(fs.readFileSync(path_file, 'utf8'));

                keys_cache = Object.keys(parsed_json_cache);

                    //Analyzing routes in cached version
                var routesCount = 0;
                var serverRouteCount = [];
                var path = [];
                for(var server in parsed_json_cache){
                    var s = {};
                    s.id = server;
                    s.name = parsed_json_cache[server].ip;
                    s.routes = [];

                    for(var route in parsed_json_cache[server].routes){
                        var p = {};
                        routesCount++;
                        p.id = parsed_json_cache[server].routes[route].IP;
                        p.addr = parsed_json_cache[server].routes[route].Addr;
                        p.time =  parsed_json_cache[server].routes[route].Time;
                        s.routes.push(p);
                        timeTaken = parsed_json_cache[server].routes[route].Time;
                    }
                    s.hops = routesCount;
                    s.timeTaken = timeTaken;
                    //console.log("Number of hops " + routesCount);
                    serverRouteCount.push(s);
                    routesCount = 0;
                        //time taken to reach the server
                }

                missedTraceRoutes = [];

                serverRouteCount.forEach(function(server){
                    if(server.timeTaken == '*'){
                      missedTraceRoutes.push(server);
                    }
                 });

                    //console.log("Missed Trace Routes: " + util.inspect(missedTraceRoutes, {depth: null}));

                    //reporting trace route analysis results
                dest_file_path = "/Users/andalpriyadarshinijayaseelan/PycharmProjects/ispViz/trace-route-analysis/generated/traceRouteStep1Extraction/trace-route-analysis_";
                dest = dest_file_path + file;
                fs.writeFile(dest, JSON.stringify(serverRouteCount, null, 2), function(err) {
                    if(err) {
                        return console.log(err);
                    }
                    count = count + 1;
                    console.log("Number of trace Route Processed Files written: " + count);
                });
            }
      });
});

