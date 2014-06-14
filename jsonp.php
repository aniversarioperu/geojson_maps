<?php

function clean_string($string) {
    $i = 0;
    if( (isset($string) && trim($string) != '') ) {
        $user_strings = array();
        $symbols = array(",",'"',"'","&","/","\\",";","=");
        #is number? then dont filter by symbols
        if( is_numeric($string) ) {
            array_push($user_strings, $string);
        }
        else { #not number, then clean by filtering symbols
            $id_subject = trim(str_replace($symbols, "", $string));
            $subject = explode(" ", $id_subject);
            foreach( $subject as $val ) {
                if( trim($val) != "" ) {
                    $pattern = '/[a-zA-Z0-9_\.\-]+/';
                    preg_match($pattern, $val, $match);
                    if( $i < 3 ) {
                        array_push($user_strings, $match[0]);
                    }
                    $i++;
                }
            }
        }
        return $user_strings;
    }
}

if( preg_match("/([a-z]+\.geojson)/", $_GET['filename'], $matches) ) {
    $filename = $matches[0];
}
else {
    exit(0);
}

$new_GET['callback'] = clean_string($_GET['callback']);
$new_GET['jsoncallback'] = clean_string($_GET['jsoncallback']);

if( isset($new_GET['callback']) ) { 
    $format = "jsonp";
    $callback = $new_GET['callback'][0];
}
if( isset($new_GET['jsoncallback']) ) {
    $format = "jsonp";
    $callback = $new_GET['jsoncallback'][0];
}

if( $format == "json" || $format == "jsonp" ) {

    if( file_exists($filename) ) {
        $file_exists = True;
    }
    else {
        exit(0);
    }

    $json = file_get_contents($filename);


    # $json = json_format(json_encode($json_output));
    header("Content-type: application/javascript; charset=utf-8");
    if( $format == "json" ) {
        echo $json;
        exit(0);
    }
    if( $format == "jsonp" ) {
        echo $callback;
        echo "(";
        echo $json;
        echo ")";
        exit(0);
    }
}
?>
