<?php
if preg_match("/([A-Z]+\.geojson)/", $_GET['filename'], $matches) {
    $filename = $matches[0];
    echo $filename;
}
else {
    echo "fail";
}

if( isset($new_GET['callback']) ) { 
    $format = "jsonp";
    $callback = $new_GET['callback'];
}
if( isset($new_GET['jsoncallback']) ) {
    $format = "jsonp";
    $callback = $new_GET['jsoncallback'];
}

if( $format == "json" || $format == "jsonp" ) {
    $json_output = array();

    $json_output['institutionCode'] = 'NSG';
    $json_output['catalogNumber'] = $row->code;
    $json_output['voucher_code'] = $row->code;
    $json_output['recordNumber'] = $row->code;
    $json_output['family'] = $row->family;
    $json_output['subfamily'] = $row->subfamily;
    $json_output['tribe'] = $row->tribe;
    $json_output['subtribe'] = $row->subtribe;
    $json_output['genus'] = $row->genus;
    $json_output['specificEpithet'] = $row->species;
    $json_output['infraspecificEpithet'] = $row->subspecies;
    $json_output['country'] = $row->country;
    $json_output['locality'] = $row->specificLocality;
    $json_output['decimalLatitude'] = $row->latitude;
    $json_output['decimalLongitude'] = $row->longitude;
    $json_output['verbatimElevation'] = $row->altitude;
    $json_output['collector'] = $row->collector;
    $json_output['eventDate'] = $row->dateCollection;
    $json_output['voucherLocality'] = $row->voucherLocality;
    $json_output['sex'] = $row->sex;
    $json_output['voucherImage'] = $row->voucherImage;

    $tmp_query = "SELECT accession FROM sequences WHERE code='$row->code'";
    $tmp_result = mysql_query($tmp_query) or die("Error in query: $tmp_query. " . mysql_error());
    if( mysql_num_rows($tmp_result) > 0 ) {
        $tmp_accessions = "";
        while( $tmp_row = mysql_fetch_object($tmp_result) ) {
            $tmp_accessions .= $tmp_row->accession . ";";
        }
    }
    $tmp_accessions = preg_replace("/;$/", "", $tmp_accessions);
    $json_output['associatedSequences'] = $tmp_accessions;

    unset($tmp_query);
    unset($tmp_result);
    unset($tmp_accessions);

    $json = json_format(json_encode($json_output));
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
