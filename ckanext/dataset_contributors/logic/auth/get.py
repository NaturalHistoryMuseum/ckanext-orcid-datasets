#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-dataset-contributors
# Created by the Natural History Museum in London, UK

from ckan.plugins import toolkit


@toolkit.auth_allow_anonymous_access
def contributor_show(context, data_dict):
    '''
    Allow for everyone.
    '''
    return {
        u'success': True
        }


@toolkit.auth_allow_anonymous_access
def contributor_autocomplete(context, data_dict):
    '''
    Allow for everyone.
    '''
    return {
        u'success': True
        }
